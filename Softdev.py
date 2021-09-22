import random

def printNames():
    pd2 = ["Mark", "Justin", "Han", "Jacob", "Jonathan", "Raymond", "Kevin", "Annabel", "Andrew", "Thomas", "Noakai"]
    pd1 = ["Angela", "Ella", "Ivan Lam", "Justin Morill", "Naomi", "Tina", "Tami" , "Christopher", "Yusuf", "Edwin", "Ishraq", "Emma", "Tomas"]
    indexPD1 = random.randint(0,len(pd1)-1)
    indexPD2 = random.randint(0,len(pd2)-1)
    FiftyPercent = random.randint(0,1)
    if (FiftyPercent == 0):
        print("Pd1 name: " + pd1[indexPD1])
    else:
        print("Pd2 name: " + pd2[indexPD2])
