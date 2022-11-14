import os
X = f"DeBelloGallicoTEST.txt_preprocessed.txt"
    # preprocessing(txt, X, proper_nouns_list, tokenizer, model)

with open(os.path.join('/home/paul/DeepL/Final/POST',X), "r") as f:
    file_1_str = f.read()

file_1_str = " ".join(file_1_str.splitlines())


print("Number of characters and tokens in",  "\t\t: ", len(file_1_str), len(file_1_str.split()))


# print(file_1_str.split())


os.chdir('/home/paul/DeepL/Final/profiles')


# FileName = input("Enter your vocab file list : ")
# my_file = open(FileName, "r")#For user input
my_file = open("Wheelock.txt", "r")
    
data = my_file.readlines() 
memory = [line.strip() for line in data]

my_file.close()

os.chdir('/home/paul/DeepL/Final/Lemma')

txt = 'DeBelloGallicoTEST.txtLemma.txt'
    
my_file = open(txt, "r")
data2 = my_file.readlines()

text = [line.split()[0] for line in data2]
my_file.close()

temp = list(set(text) - set(memory)) 
    
res = [ ele for ele in text ]
for a in text:
    if a in memory:
        res.remove(a)

print(len(res)/len(text)*100)