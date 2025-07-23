import pandas as pd
import numpy as np
from function import *
from sklearn.model_selection import train_test_split


path = "PATH_TO_DATA"

# Load data & Clean columns
df= pd.read_csv(path, sep= ";", header= 0)
df= df.drop(columns = ['']) #Drop columns if needed such as Unnamed columns
df = df.dropna()
print(df.columns) # check name of the characters column and quote column here it's "author" and "dialogue"
df['author'] = df['author'].str.lower()

################################################################################
# Preprocess the data
################################################################################
#Critere 1 :: Remove parentheses from inside the dialogue
df = df.copy()
df['dialogue'] = df['dialogue'].apply(remove_parentheses)

## Critere 2 ::dialogue lenght should be bigger than 5 words  
ind_remove =  df[df['dialogue'].str.split().str.len() < 5].index 
df = df.drop(ind_remove, inplace=False) # anything less than 5 to be remove 

## Critere 3 :: the character should have at least 100 sentencs 
value_counts = df['author'].value_counts()
to_remove = value_counts[value_counts <= 99].index

# Critere 3 :: remove non character lines such as "scense" that discribe the scene
to_remove = to_remove.tolist() + ["(off)", "Scene"]
ind_remove = df[df['author'].isin(to_remove)].index
df.drop(ind_remove, inplace=True)


##Critere 4 ::split if there multiple sentences 
df.apply(lambda x:split_quotes(x), axis=1)

##Critere 5 :: remove any unwnated symbols  
mask = df['dialogue'].str.contains('\(|\)') # backslashes escape parentheses
df.drop(df[mask].index, inplace = True)

# Check the shape of the dataframe after preprocessing
df.reset_index(drop=True, inplace=True)
print("Shape Of datbase after Preprocessing :: " + str(df.shape))

# Save the preprocessed dataframe to a csv file
df.to_csv("preprocessed_data.csv", index=False)

################################################################################
#Split the dataframe into train and test sets
################################################################################

## split based on the 15% of each character or max_sample to have a blanced test set

max_sample = 110 
for person, count in df['author'].value_counts().items(): 
    print("{} ===> {}".format(person,count))
    
    sample_size = int(min(np.ceil(count * 0.15), max_sample))
    # Take a random sample of rows with for this person
    sample_df = df[df['author'] == person].sample(n=sample_size, random_state=124)
    
    # Append the sample to the sampled dataframe
    sampled_df = pd.concat([sampled_df,sample_df])

# Drop the sampled rows from the original dataframe
train_all_tbbt = df.drop(sampled_df.index)

# Reset the index of the dataframes
sampled_df = sampled_df.reset_index(drop=True)
train_all_tbbt = train_all_tbbt.reset_index(drop=True)

## Save the train and test sets to csv files
sampled_df.to_csv("test_data.csv", index=False)
train_all_tbbt.to_csv("train_data.csv", index=False)

