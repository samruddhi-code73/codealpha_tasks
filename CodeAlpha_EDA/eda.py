import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('amazon.csv')
df.head()
df.shape
df.columns
df.info()
df.describe()

df['actual_price'] = (
    df['actual_price']
    .str.replace('â‚¹', '', regex=False)
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)
df['discounted_price'] = (
    df['discounted_price']
    .str.replace('â‚¹', '', regex=False)
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

df['discount_percentage'] = df['discount_percentage'].str.replace('%','')
df['discount_percentage'] = df['discount_percentage'].astype(float)

df['rating']=pd.to_numeric(df['rating'],errors='coerce')

df['rating_count'] = df['rating_count'].str.replace(',','')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

df.isnull().sum()
df.dropna(inplace=True)
df.to_csv('clean_amazon.csv',index=False)




