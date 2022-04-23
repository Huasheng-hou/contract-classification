import pandas as pd
import numpy as np

from ltp import LTP

corpus = pd.read_csv('corpus.csv')
texts = np.array(corpus['正文'])

ltp = LTP()
seg, hidden = ltp.seg(list(texts)[:1])

pos = ltp.pos(hidden)
ner = ltp.ner(hidden)
srl = ltp.srl(hidden)
dep = ltp.dep(hidden)
sdp = ltp.sdp(hidden)

entities = [seg[0][n[2]] for n in ner[0]]
npos, nouns = [], []

for idx, p in enumerate(pos[0]):
    if 'n' in p and p not in ['ng', 'nr', 'ns', 'nz', 'nh', 'nt']:
    # if 'n' in p:
        npos.append(p)
        nouns.append(seg[0][idx])

for idx, p in enumerate(npos):
    print(p, nouns[idx])
