import glob 
import re
from preprocessing import preprocessing
from fileinput import filename
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from tqdm import tqdm
import os

tokenizer = AutoTokenizer.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
model = AutoModelForTokenClassification.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
os.chdir('/home/paul/DeepL/Final/Nouns')
proper_nouns_file = "proper_nouns_names.txt"
proper_nouns_list = open(proper_nouns_file).read().lower().splitlines()

os.chdir('/home/paul/DeepL/Final/LatLib')

for txt in list(glob.glob("*.txt")):

    print(txt)
    X = f"{txt}_preprocessed.txt"
    preprocessing(txt, X, proper_nouns_list, tokenizer, model)