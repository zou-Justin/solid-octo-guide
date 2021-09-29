# K06--CSV README

Mark Zhu, Justin Zou, Han Zhang (Team MJH)
---

# File I/O
We read our file by opening up and setting it as csvfile(variable name).
Using the csv library, we open up our file using dictReader() which automatically converts every line in the file into a dictionary.
Then we can parse through each line and set the float values to each occupation in our own dictionary.
Input was the file, output were the rows as dictionaries that we convert to a dictionary.

# Dictionaries
A dictionary was particulary useful in this assignment because we could assign a key value pair, with job occupatioon as the key and percentage as the pair.
Since we are using a dictionary, we can easily get both of these values and use them accordingly.

# List
We didn't use a list because it doesn't store pairs as easily as Dictionaries. However, they are useful in collecting values and relating them to a specific index. They are easily changeable and easy to access.

# GitHub Markdown
Adding a "#" allows you to bolden the title and creates a horizontal line at the bottom useful for separation.

# How our random selection worked
1) First we had a two variable for loop go through each pair of items in the dictionary. 
2) Then, We generated a random float value using the random library, between 0 and 99.8(the sum of all percentages). 
3) Next, We had a variable x that was set to 0 which is the lower limit for the percentage while x + percentage value is the upper bound. 
4) If the randomized number falls between that range, then we print the occupation related to that percentage.
5) If not, we increase x by that percentage value and try again with the next percentage, until the random float value we generated is in the range.
