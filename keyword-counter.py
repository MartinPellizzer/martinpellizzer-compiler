import numpy as np
import pandas as pd

with open('keywords/ozone-scrape-copy.txt', encoding='utf-8') as f:
    content = f.read()

words = content.replace('\n', ' ').split()

# words = ['hello', 'goodbye', 'howdy', 'hello', 'hello', 'hi', 'bye']

df = pd.value_counts(np.array(words))
df.to_csv('out.csv')