import pandas as pd
from collections import Counter
import re

df = pd.read_csv('online_retail/online_retail_II_clean_2011.csv')
df['Processed_Description'] = df['Description'].str.lower()
df['Processed_Description'] = df['Processed_Description'].apply(lambda x: re.sub(r'\W+', ' ', x))
df['Words'] = df['Processed_Description'].str.split()

all_words = [word for words_list in df['Words'] for word in words_list]
word_counts = Counter(all_words)


print(word_counts.most_common(100))
