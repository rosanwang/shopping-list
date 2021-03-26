import requests
import os
import pandas as pd
from bs4 import BeautifulSoup 
import re; 
import unicodedata; 


keywords = ["cups", "cup",  "tablespoons", "tablespoon", "teaspoons", "teaspoon", "pound"]

def findIngredients(url):
    array = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ingredients = soup.find_all(class_='ingredients-item-name')
    
    
    for i in ingredients :
        str = useless_keywords(i.get_text()).strip()
        array.append(str.split(",")[0])
    return array

def findMeasurements(ingred):

    measurements = {}
    for x in ingred :
        w = has_key_word(x)
        if w != "":
            parse = x.split(w)
            key = parse[1].strip()
                #unicodedata.numeric()
            value = (parse[0] + w).strip()
            measurements[key] = value
        else :
            x = x.strip()
            #TODO: handle double digit values? decimals?
            value = x[0]
            key = x[1:len(x)].strip()

            if (isNum(value) == False) :
                # represent data types without number as 1 + "ingredient name"
                value = "1"
                key = x.strip()
            measurements[key] = value       
    
    '''
        for w in keywords :
            parse = x.split(w)
            print(parse)
            if len(parse) != 1 :
                key = parse[1].strip()
                #unicodedata.numeric()
                value = (parse[0] + w).strip()
                measurements[key] = value
            else :
                x = x.strip()
                value = x[0]
                key = x[:len(x)]
                measurements[key] = value
        '''
    return measurements


def isNum(value):
    hasnum = False
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in nums:
        if (value.find(i) != -1):
            hasnum = True
    return hasnum


def has_key_word(ingredient): 
    for w in keywords :
        if (len(ingredient.split(w)) != 1):
            return w 
    return ""

#TODO add more keywords which are not needed 
def useless_keywords(str):
    num = str.find("to taste")
    if (num != -1):
        #currently returns the string before the key word -> maybe to taste will be in the middle?? 
        return str[:num]
    return str

def main():
    fm = findMeasurements(findIngredients("https://www.allrecipes.com/recipe/220250/chef-johns-deviled-eggs/"))

    print(fm)
    #print(len(fm))

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
