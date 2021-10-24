# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev 
# K16: All About Database - skeleton/stub :: SQLITE3 BASICS 
# 2021-10-25

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# -- courses.csv

# Creates the table with the correct column names and types
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

with open("courses.csv", "r") as courses_file: # opens courses.csv
    # reads the csv file and converts each row into a dictionary, name of the column is set equal to the value at the row
    reader = csv.DictReader(courses_file) 
    for row in reader:
        # f-strings were used to make commands more readable
        # instead of using string concatenation

        # The repr() function, when called with a string,
        # automatically adds quotes around them.
        command = f"""
            INSERT INTO courses VALUES
              ({repr(row['code'])},
               {row['mark']},
               {row['id']})
        """
        # print("***DIAG: command ***") 
        # print(command)
        c.execute(command) 

# -- students.csv
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)") 

with open("students.csv", "r") as students_file: # opens students.csv
    reader = csv.DictReader(students_file) 
    for row in reader:
        command = f"""
            INSERT INTO students VALUES
              ({repr(row['name'])},
               {row['age']},
               {row['id']})
        """
        # print("***DIAG: command ***") 
        # print(command)
        c.execute(command) 

#==========================================================

db.commit() #save changes
db.close()  #close database
