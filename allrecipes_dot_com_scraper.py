import os
import requests
from bs4 import BeautifulSoup
from usp.tree import sitemap_tree_for_homepage
import json


def scrap_to_json(raw_data_dir_name, n_recipes=10):

    """ 
    Scraping allrecipes.com to json files

    Keyword arguments:
    raw_data_dir_name -- the address to save the raw data
    n_recipes -- the number of recipes to be saved, pass 'all'
    to save all the recipes. The default value is 10
    
    Creates and saves(json) one dict per recipe with the following keys:
    recipt_id: an integer which is the id of the recipe on the website
    name: a string, name with - as the separator
    url: a string
    ingredients: a list of strings where each string has both
    ingredient name and the amount. This should be changed to
    a dictionary where key is the ingredient name and value is
    the amount
    nutritions: a dictionary with the keys->nutrient name and
    values-> the amount
    """

    if (n_recipes == 'all'):
        scrap_all = True
    else:
        scrap_all = False
        
    tree = sitemap_tree_for_homepage('https://www.allrecipes.com/recipe/')

    for counter, page in enumerate(tree.all_pages()):
        if (scrap_all or counter < n_recipes):
            url = page.url
            print(url)
            recipte_id = url.split('/')[4]
            name = url.split('/')[5]
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features='html.parser')
            all_ingredients = soup.find_all('span', attrs={'class': 'ingredients-item-name'})
            ingradients_list = []
            for ingradient in all_ingredients:
                tmp = ingradient.text
                tmp = tmp.replace('\n', '')
                tmp = tmp.replace('  ', '')
                tmp = tmp.strip()
                #print(tmp)
                ingradients_list.append(tmp)

            all_nutrition = soup.find_all('span', attrs={'class': 'nutrient-name'})
            nutrient_dict = {}
            for nut_with_value in all_nutrition:
                nut_with_value_text = nut_with_value.get_text().replace('\n', '').replace('  ', ' ').strip().split(':')
                nut_name = nut_with_value_text[0].strip()
                nut_value = nut_with_value_text[1].strip()
                nutrient_dict[nut_name] = nut_value

            raw_data = {'id': recipte_id, 'name': name, 'url' : url, 'ingradients' : ingradients_list, 'nutritions' : nutrient_dict}
            raw_data_file_name = os.path.join(raw_data_dir_name, recipte_id+'.json')
            with open(raw_data_file_name, 'w') as fp:
                json.dump(raw_data, fp)
    pass
