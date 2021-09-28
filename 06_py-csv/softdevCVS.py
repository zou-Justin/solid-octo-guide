# Mark Zhu, Justin Zou, Han Zhang (Team MJH)
# SoftDev
# K06 -- StI/O: Divine your Destiny!
# 2021-09-28

import random
import csv


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
