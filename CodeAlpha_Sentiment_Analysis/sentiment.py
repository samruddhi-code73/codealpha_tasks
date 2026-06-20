import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


df = pd.read_csv('amazon_reviews.csv')

def get_polarity(text):
    return TextBlob(str(text)).sentiment.polarity

df['polarity'] = df['reviewText'].apply(get_polarity)

df['sentiment'] = df['polarity'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

sns.countplot(data=df, x='sentiment', ax=axes[0, 0])
axes[0, 0].set_title('Sentiment Distribution')

sns.boxenplot(data=df, x='sentiment', y='overall', ax=axes[0, 1])
axes[0, 1].set_title('Rating by Sentiment')

pos_text = ' '.join(df[df['sentiment'] == 'Positive']['reviewText'].dropna())

if len(pos_text) > 10:
    wc = WordCloud(background_color='white').generate(pos_text)
    axes[1, 0].imshow(wc)
    axes[1, 0].axis('off')
else:
    axes[1, 0].text(0.5, 0.5, 'No positive reviews', ha='center')

axes[1, 0].set_title('Positive Words')

top_authors = df['reviewerName'].value_counts().head(5)
sns.barplot(x=top_authors.values, y=top_authors.index, ax=axes[1, 1])
axes[1, 1].set_title('Top Reviewers')

df[['reviewText', 'overall', 'sentiment', 'polarity']].to_csv('amazon_sentiment.csv', index=False)
plt.savefig('charts.png')

plt.show()
