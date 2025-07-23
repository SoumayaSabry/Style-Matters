#this file contion Function to preprocess the data

import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import re



# Split dialogue into individual quotes using NLTK's sent_tokenize function.
# If there are multiple quotes or sentence ending with "." in a single dialogue, split them into separate rows
# and append them to the global dataframe df_TBBT.

def split_quotes(raw):
  global  df_TBBT
  split_dialogue = sent_tokenize(raw.dialogue)
  if len(split_dialogue) > 1:
    raw.dialogue = split_dialogue[0]
    for i in range(1,len(split_dialogue)):
      if len(split_dialogue[i]) > 5:
        new_row = pd.DataFrame({'episode_name':[raw.episode_name], 
                                'dialogue':[split_dialogue[i]], 
                                'person_scene': [raw.person_scene]})
        df_TBBT = pd.concat([df_TBBT, new_row], ignore_index=True)
      #df_TBBT = df_TBBT.append(new_row, ignore_index=True)

# Define a function to limit sentence words
def limit_nb_words(raw , limit):
  words = raw.dialogue.split()
  if len(words) > limit+1:
    raw.dialogue = " ".join(words[:limit]) 

# Define a function to remove parentheses from text
def remove_parentheses(text):
    return re.sub("\(.*?\)", "", text)