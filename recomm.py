import pandas as pd

# Import dataset
df = pd.read_csv('sample.csv')

df.dropna()
df.info()
#X =df[['Age(Yrs.)','Weight(Kg)','Height (ft.)','Diseases_code']].values
#y1 =df['Breakfast_code'].values
#y2 =df['Lunch_code'].values
#y3 =df['Dinner_code'].values
#from sklearn.linear_model import LogisticRegression
#model =LogisticRegression(solver='liblinear')
#model.fit(X,y1)