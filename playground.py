import pandas as pd
import numpy as np

from ltp import LTP

ltp = LTP()

f = pd.read_excel('data/contract_notation.xlsx')
samples = []

for idx, row in f.iterrows():

    cls_idx = 0
    text = row['Contract']
    seg, hidden = ltp.seg([text])
    seg = seg[0]
    locs = []
    start = 0
    classes = np.zeros(len(seg))
    for s in seg:
        locs.append(start)
        start += len(s)

    for col, item in row.iteritems():
        if 'Keywords' in col or 'Key words' in col:
            cls_idx += 1
            word = item
            if not isinstance(word, str) or word == '/':
                continue
            print(word)
            loc = text.find(word)
            print(loc)
            if loc != -1 and loc in locs:
                s_loc = locs.index(loc)
                classes[s_loc] = cls_idx

    samples.append(','.join(seg))
    samples.append(','.join(list(classes.astype(int).astype(str))))
    print('====================================')

data = pd.DataFrame({
    'samples': samples,
})

data.to_csv('data/samples.csv', index=False)
