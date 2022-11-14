import re

def removeMacrons(string):
    """"
    Removes the macrons from any macron-ed characters in a string.

    Parameters:
        string (str): the string whose macrons are to be removed
            macrons must be separated as combining characters

    Returns:
        (str): string without any macrons
    """

    return re.sub('\u0304', '', string)

import requests
from lxml import html

my_file = open("Wheelock.txt", "r")

data = my_file.readlines() 
memory = [line.strip() for line in data]

my_file.close()


my_file = open("DeBelloGallicoLemma.txt", "r")
data2 = my_file.readlines()

text = [line.split()[0] for line in data2]
my_file.close()

#print(text)

temp = list(set(text) - set(memory)) 


# print(temp)


res = [ ele for ele in text ]
for line in res:
    print("https://en.wiktionary.org/wiki/" + str(line) + "#Latin")

print(len(res)/len(text))



import googletrans
from googletrans import Translator

translator = Translator()


my_file = open("DeBelloGallicoLemma.txt", "r")
data2 = my_file.readlines()

text = [line.split()[0] for line in data2]
my_file.close()

temp = list(set(text) - set(memory)) 
print(len(temp))
words = []

for i in temp:
    result = translator.translate(i)
    print(result.text)
    words.append(result.text)

print(words)