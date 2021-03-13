import requests
import os
import pandas as pd
from bs4 import BeautifulSoup 
import re; 
import unicodedata; 


keywords = ["cup", "tablespoon", "tablespoons", "teaspoon", "teaspoons", "pound", "cups"]

def findIngredients(url):
    array = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ingredients = soup.find_all(class_='ingredients-item-name')
    
    
    for i in ingredients :
        str = i.get_text()
        array.append(str.split(",")[0])
    return array

def findMeasurements(ingred):

    measurements = {}
    for x in ingred :
        for w in keywords :
            parse = x.split(w)
            if len(parse) != 1 :
                key = parse[1].strip()
                #unicodedata.numeric()
                value = (parse[0] + w).strip()
                measurements[key] = value
        
        x = x.strip()
        value = x[0]
        print(value)
        key = x[:len(x)]
        print(key)
        measurements[key] = value

        #split at the numberpip inst
    return measurements



def main():
    fm = findMeasurements(findIngredients(
        "https://www.allrecipes.com/recipe/267578/airline-chicken-breast/"))

    #print(fm)

if __name__ == '__main__':
    main()
    


#map 1/2 glif to 0.5 (is there a function for this?)
#convert unicode to str?
#ingredients that are differently named but the same thing ?

#measurements: find num (or fraction, whatever comes first), if word after  num is in measurement array, return num + word after 
#if not, 
          # fraction?  contain "/" -> include in num 
       # else return word after as ingredient name 

#python web framework? 
    # flask -> harder for frontend programming 
    #html documents called templates (inject python variables into)

#react.js 
    # seperated frontend and backend 
