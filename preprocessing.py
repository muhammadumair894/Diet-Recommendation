import numpy as np
import pandas as pd

# Import dataset
df = pd.read_csv('CDataset.csv')
print(df.head(5))
#df.replace(to_replace="Hypertension patient", value="Hypertension")
#print(df['Diseases '].unique())
Dis = df['Lunch']
#df['Diseases '].unique()
Dis.str.strip()
print(Dis)
#print(Dis.unique())
from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
df["Lunch_code"] = lb_make.fit_transform(df["Lunch"].astype(str))
print(df[["Lunch", "Lunch_code"]].head(111))