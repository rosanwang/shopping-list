import requests
import os
import pandas as pd
from bs4 import BeautifulSoup 
import re; 

page = requests.get("https://www.allrecipes.com/recipe/256019/orange-cranberry-bundt-cake/")

soup = BeautifulSoup(page.content, 'html.parser')

#fieldset = soup.find('fieldset', class_='ingredients-section__fieldset')

ingredients = soup.find_all(class_='ingredients-item-name')

#how to get multiple sections 

#file = open(os.getcwd() + "read.txt", "w")

listOfIngred = ""

measurements = ["cup, tablespoon, teaspoon, pound"]

for i in ingredients :
    #print(i.get_text())
    str = i.get_text
    try: 
        re.search(",", str)
    except 
        listOfIngred = listOfIngred + i.get_text()
    #file.write(i.get_text())
    #File_object.write()




#measurements: find num (or fraction, whatever comes first), if word after  num is in measurement array, return num + word after 
#if not, 
          # fraction?  contain "/" -> include in num 
       # else return word after as ingredient name 

print(listOfIngred)
#file.close()