import glob 
import re
from preprocessing import preprocessing
from fileinput import filename
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from tqdm import tqdm
import os
import sys

tokenizer = AutoTokenizer.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
model = AutoModelForTokenClassification.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
os.chdir('/home/paul/DeepL/Final/Nouns')
proper_nouns_file = "proper_nouns_names.txt"
proper_nouns_list = open(proper_nouns_file).read().lower().splitlines()

os.chdir('/home/paul/DeepL/Final/Examp')

for txt in list(glob.glob("*.txt")):

    print(txt)
    X = f"{txt}_preprocessed.txt"
    # preprocessing(txt, X, proper_nouns_list, tokenizer, model)

    with open(os.path.join('/home/paul/DeepL/Final/POST',X), "r") as f:
        file_1_str = f.read()

    file_1_str = " ".join(file_1_str.splitlines())


    print("Number of characters and tokens in", txt, "\t\t: ", len(file_1_str), len(file_1_str.split()))


    print(file_1_str.split())
    sys.exit()

    def lemma_count(words):
        lemma_dict = {}
        for item in words:
            if item.lemma not in lemma_dict:
                lemma_dict[item.lemma] = 1
            else:
                lemma_dict[item.lemma] += 1
        
        lc = clean_lemma_counts(sorted(lemma_dict.items(), key=lambda kv: kv[1], reverse=True))
        return lc
        
    def clean_lemma_counts(lemma_counts):
        lc = [] # new list of tuples with lemma and count
        non_use = []
        for lemma, count in lemma_counts:
            if((re.search(r'[^\w\s]', lemma))): #checks if there is punc
                non_use.append(lemma)
            else: # if no punc, add to new list
                new_tup = (lemma, count)
                lc.append(new_tup)
                
        print(len(non_use)) # keeps track of how many lemmas we are removing
        return lc    

    #certain amount of most frequent words from whole corpus
    #check words against that a given text
        #do that with each text
        #deliver a percentage of how much overlap
            #score for text
            #higher scores are for more easy learning 
            #lower scores are probably impossible 


    #get lemma counts for both text files
    #add lemma counts together, if two tuples have the same lemma, add the counts to one, and remove the other
    #we then have the corpus


    lemma_counts = lemma_count(cltk_doc1.words)

    with open(os.path.join('/home/paul/DeepL/Final/Lemma',f'{txt}Lemma.txt'), "w") as f:
        for t in lemma_counts:   
            f.write(' '.join(str(s) for s in t) + '\n')

    # os.chdir('/home/paul/DeepL/Final/Examp')
    # textfile = open(f'{txt}Lemma.txt', 'w')
    # f=textfile

    # for t in lemma_counts:   
    #     f.write(' '.join(str(s) for s in t) + '\n')

    # f.close()

os.chdir('/home/paul/DeepL/Final/profiles')


# FileName = input("Enter your vocab file list : ")
# my_file = open(FileName, "r")#For user input
my_file = open("Wheelock.txt", "r")
    
data = my_file.readlines() 
memory = [line.strip() for line in data]

my_file.close()

os.chdir('/home/paul/DeepL/Final/Lemma')

for txt in glob.glob("*Lemma.txt"):
    
    my_file = open(txt, "r")
    data2 = my_file.readlines()

    text = [line.split()[0] for line in data2]
    my_file.close()

    temp = list(set(text) - set(memory)) 
    
    res = [ ele for ele in text ]
    for a in text:
        if a in memory:
            res.remove(a)

    # print("The Subtracted list is : " + str(res))

    # print(f"The percent of known from the text: {txt} is: {len(temp)/len(text)}")