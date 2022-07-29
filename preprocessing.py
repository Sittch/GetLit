from fileinput import filename
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from tqdm import tqdm

import re

def RegEX(string):
    file_1_str = re.sub(r"[([{})]]", "", string) #removing brackets
    file_1_str = re.sub("\d+", "", file_1_str) #removing numbers
    return re.sub('\u0304', '', file_1_str)

def preprocessing(file_name, out_file, proper_nouns_list, tokenizer, model):
  # tokenizer = AutoTokenizer.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
  # model = AutoModelForTokenClassification.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
  # proper_nouns_file = "proper_nouns_names.txt"
  # proper_nouns_list = open(proper_nouns_file).read().lower().splitlines()
  in_file = open(file_name, 'r')
  input_file = in_file.read().splitlines()
  out_file = open(out_file, 'w')
  for i, line in enumerate(tqdm(input_file)): 
    # Checking if it not an empty line
    if(len(line) > 0):
      # Tokenize string
      result = tokenizer.tokenize(line)
      # print(line)
      # print(result)

      # Encode tokens 
      tokens_tensor = tokenizer.encode(line, add_special_tokens=False, return_tensors="pt")
      attention_mask = torch.ones(tokens_tensor.size())

      # Run the model and get predicted POS 
      outputs = model(tokens_tensor, attention_mask)
      predicted_class_ids = outputs.logits.argmax(-1)
      predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_class_ids[0]]
      # print(predicted_tokens_classes)

      # Remove proper nouns based on latin pos pretrained model
      words = line.split()
      word_num = -1
      proper_noun = False
      for j in range(len(predicted_tokens_classes)):
        if(result[j][0] == '▁'):
          word_num += 1
          if (word_num != 0 and proper_noun == True):
            words.pop(word_num - 1)
            word_num -= 1
            proper_noun = False
        if (predicted_tokens_classes[j] == 'PROPN'):
          proper_noun = True
      if (proper_noun == True):
        words.pop(-1)

      # Remove words in the proper noun list 
      words_without_propn = []
      for word in words: 
        if word.lower() not in proper_nouns_list: 
          words_without_propn.append(word)

      # Lowercase and remove macrons             
      line_propn_removed = " ".join(words_without_propn)
      line_propn_removed_lowered = line_propn_removed.lower() 
      line_propn_removed_lowered_macrons_removed = RegEX(line_propn_removed_lowered)
      out_file.write(f"{line_propn_removed_lowered_macrons_removed}\n")
      # print(line_propn_removed_lowered_macrons_removed)
    else: 
      # print()
      out_file.write("\n")
    # if i == 20: 
    #   break
  in_file.close()
  out_file.close()

# proper_nouns_file = "proper_nouns_names.txt"
# proper_nouns_list = open(proper_nouns_file).read().lower().splitlines()
# print(proper_nouns_list)

# file_1 = "AeneidTEST.txt"
# file_2 = "DeBelloGallicoTEST.txt"
# tokenizer = AutoTokenizer.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")
# model = AutoModelForTokenClassification.from_pretrained("wietsedv/xlm-roberta-base-ft-udpos28-la")

# file_1_preprocessed = "preprocessed_aeneid.txt"
# preprocessing(file_1, file_1_preprocessed, proper_nouns_list, tokenizer, model)
