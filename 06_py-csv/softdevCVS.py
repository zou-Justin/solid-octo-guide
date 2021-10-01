# Mark Zhu, Justin Zou, Han Zhang (Team MJH)
# SoftDev
# K06 -- StI/O: Divine your Destiny!
# 2021-09-28

import random
import csv


#We read our file by opening up and setting it as csvfile(variable name). 
#Using the csv library, we open up our file using dictReader() which automatically converts every line in the file into a dictionary. 
#Then we can parse through each line and set the float values to each occupation in our own dictionary. 
#Input was the file, output were the rows as dictionaries that we convert to a dictionary.


randomNum = random.random()* 99.8
dict = {}
    
with open("occupations.csv", mode = 'r') as csvfile:
    csv = csv.DictReader(csvfile)

    for lines in csv:
        dict[lines['Job Class']] = float(lines['Percentage'])

x = 0.0
for i, j in dict.items():
    if x <= randomNum < x + j:
        print (i)
    x += j
