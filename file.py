import pandas as pd
from docx.api import Document

document = Document('dataset.docx')
table = document.tables[0]

data = []

keys = None
c =0
for i, row in enumerate(table.rows):
    text = (cell.text for cell in row.cells)
    c = c+1
    if i == 0:
        keys = tuple(text)
        continue
    row_data = dict(zip(keys, text))
    data.append(row_data)
    print (c)
    if c ==10:
        break

df = pd.DataFrame(data)
df.to_csv("dataset2.csv", encoding='utf-8', index=False)