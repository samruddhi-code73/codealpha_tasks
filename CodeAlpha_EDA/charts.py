import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('clean_amazon.csv')
df.head()

sns.histplot(df['rating'],bins=20)
plt.title('Distribution of Product Ratings')
plt.show()

sns.histplot(df['discount_percentage'], bins=20)
plt.title('Discount Percentage Distribution')
plt.show()

top_categories = df['category'].value_counts().head(10)

top_categories.plot(kind='bar')
plt.title('Top 10 Product Categories')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(8,5))

sns.heatmap(
    df[['actual_price','discounted_price',
        'discount_percentage','rating',
        'rating_count']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.show()

sns.boxplot(x=df['actual_price'])
plt.show()


top_rated = df.sort_values(by='rating', ascending=False)

top_rated[['product_name','rating']].head(10)

highest_discount = df.sort_values(
    by='discount_percentage',
    ascending=False
)

highest_discount[['product_name',
                  'discount_percentage']].head(10)

correlation = df['discount_percentage'].corr(df['rating'])

print(correlation)



