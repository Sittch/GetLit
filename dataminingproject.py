import re

file_1 = "AeneidTEST2.txt"
file_2 = "DeBelloGallicoTEST2.txt"
file_1_str = " ".join(open(file_1).read().splitlines())
file_2_str = " ".join(open(file_2).read().splitlines())

print("Number of characters and tokens in", file_1, "\t\t: ", len(file_1_str), len(file_1_str.split()))
print("Number of characters and tokens in", file_2, "\t: ", len(file_2_str), len(file_2_str.split()))

len(set(file_1_str.split()))

# First run causes ContexualVersionConflict. 
from cltk import NLP
cltk_nlp = NLP(language="lat")

# Removing ``LatinLexiconProcess`` for this demo b/c it is slow (adds ~9 mins total)
cltk_nlp.pipeline.processes.pop(-1)
print(cltk_nlp.pipeline.processes)

# Commented out IPython magic to ensure Python compatibility.
cltk_doc1 = cltk_nlp.analyze(text=file_1_str)

# Commented out IPython magic to ensure Python compatibility.
cltk_doc2 = cltk_nlp.analyze(text=file_2_str)

#cltk_doc1.lemmata[:100]
cltk_doc1.words[0].lemma

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
from collections import Counter

lemma_counts = lemma_count(cltk_doc1.words)
lemma_counts2 = lemma_count(cltk_doc2.words)

def add_corpora(lemma_counts, lemma_counts2):
    #get dics of lemmas and counts
    #make copies?
    dict_lemmas1 = dict(lemma_counts)
    dict_lemmas2 = dict(lemma_counts2)
       
    #check to see if the word already exists in one of the corpora
    #merge two dictionaries
    merged_dic = Counter(dict_lemmas1)+Counter(dict_lemmas2)
    merged_lemmas = sorted(merged_dic.items(),key=lambda kv:kv[1],reverse=True)
    return merged_lemmas

                
def get_lemmas(lemma_counts):
    lemmas = []
    for lemma, count in lemma_counts:
        lemmas.append(lemma)
    return lemmas
        
def get_counts(lemma_counts):
    counts = []
    for lemma, count in lemma_counts:
            counts.append(count)
    return counts
        

#demarcate subsection of corpus as what the reader knows
#compare the subsection of the corpus with the vocabulary (number of unique words)
#compute score 



#decide what scores are easy and what are hard

corpora = add_corpora(lemma_counts, lemma_counts2)


print(lemma_counts)


textfile = open('AeneidLemma.txt', 'w')
f=textfile

for t in lemma_counts:   
  f.write(' '.join(str(s) for s in t) + '\n')

f.close()

textfile = open('DeBelloGallicoLemma.txt', 'w')
f=textfile

for t in lemma_counts2:
  f.write(' '.join(str(s) for s in t) + '\n')

f.close()

textfile = open('Lemma.txt', 'w')
f=textfile

for t in corpora:
  f.write(' '.join(str(s) for s in t) + '\n')

f.close()