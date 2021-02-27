import requests
import os
import pandas as pd
from bs4 import BeautifulSoup 

page = requests.get("https://www.allrecipes.com/recipe/256019/orange-cranberry-bundt-cake/")

soup = BeautifulSoup(page.content, 'html.parser')

fieldset = soup.find('fieldset', class_='ingredients-section__fieldset')

ingredients = fieldset.find_all(class_='ingredients-item-name')

#how to get multiple sections 

file = open(os.getcwd() + "read.txt", "w")

for i in ingredients :
    file.write(i.get_text())
    #File_object.write()
    #print(i.get_text())

file.close()