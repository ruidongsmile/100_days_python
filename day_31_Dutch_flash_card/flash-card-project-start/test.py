import pandas as pd

df1 = pd.read_csv("data/dutch_words.csv")
print(df1.shape)

df2 = pd.read_csv("data/words_to_learn.csv")
print(df2.shape)