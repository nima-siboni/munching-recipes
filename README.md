# munching-recipes

Web scraping www.allrecipes.com and returning info in form of Python dictionaries.

## requirements
* os
* requests
* json
* BeautifulSoup
* ultimate_sitemap_parser 


```
pip install -r requirements.txt
```
## description
For each recipe a separate dictionary is savedin the ~/raw_data_sets/recipes as a json file. Each dictionary has the following items:
* recipt_id: an integer which is the id of the recipe on the website
* name: a string, name with - as the separator
* url: a string
* ingredients: a list of strings where each string has both ingredient name and the amount. This should be changed to a dictionary where key is the ingredient name and value is the amount nutritions: a dictionary with 
 the keys->nutrient name and values-> the amount

## usage
```
python3 scrap_all_recipes.py
```
and your json files will be in 
```
~/raw_data_sets/recipes
```
