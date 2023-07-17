import numpy as np
import pandas as pd

def word_counter():
    with open('keywords-todo.txt', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    words = content.split()
    print(words)

    df = pd.value_counts(np.array(words))

    df.to_csv('words-count.csv', encoding='utf-8')



# word_counter()