import pandas as pd
import numpy as np

from ltp import LTP

samples = pd.read_csv('data/samples.csv')

ltp = LTP()
seg, hidden = ltp.seg(list(samples['keyword']))

for s in seg:
    print(s)
