import pandas as pd
import numpy as np


f = pd.read_excel('heyue_fx1.xlsx')
corpus = f['正文']

corpus.to_csv('corpus.csv')

# maxlen = -1
# lens = []
#
# for d in corpus:
#     if len(d) > maxlen:
#         maxlen = len(d)
#     lens.append(len(d))
