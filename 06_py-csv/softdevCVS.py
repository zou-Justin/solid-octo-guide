import random
import csv

def main():
    randomNum = random.random()* 99.8
    
    with open("occupations.csv", newline='') as csvfile:
        Dictionary = csv.DictReader(csvfile)
    x = 0.0
    for i, j in Dictionary.items():
        if x <= randomNum < x + j:
            print (i)
        x += j
        
