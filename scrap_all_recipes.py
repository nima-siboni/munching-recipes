import os
from allrecipes_dot_com_scraper import scrap_to_json

# This script scraps allrecipes.com for info
# 0 - (preambles) creating the directory to save the raw data
# 1 - web scraping the allrecipes.com for recipes, their ingredients
# and nutrition values

# 0
home = os.environ['HOME']
raw_data_dir_name = os.path.join(home, 'raw_data_sets', 'recipes')
os.makedirs(raw_data_dir_name, exist_ok=True)

# 1

# the second argument for the scrap_to_json is the number of recipes
# to be scraped. The default value is 10, and if 'all' is passed, the
# function takes all the recipes.
scrap_to_json(raw_data_dir_name)
