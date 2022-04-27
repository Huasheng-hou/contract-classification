import pandas as pd

f = pd.read_excel('data/contract_notation.xlsx')
cls_idx = 0
samples, classes = [], []

for col in f.columns:
    if 'Keywords' in col or 'Key words' in col:
        cls_idx += 1
        print(col)
        words = f[col].dropna()
        print(words)
        for w in words:
            if w == '/':
                continue
            samples.append(w)
            classes.append(cls_idx)

data = pd.DataFrame({
    'keyword': samples,
    'class': classes,
})

data.to_csv('data/samples.csv', index=False)
