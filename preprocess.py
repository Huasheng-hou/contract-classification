import pandas as pd
import numpy as np

from ltp import LTP

corpus = pd.read_csv('corpus.csv')
texts = np.array(corpus['正文'])

ltp = LTP()
seg, hidden = ltp.seg(list(texts)[:1])
ner = ltp.ner(hidden)

entities = [seg[0][n[2]] for n in ner[0]]
