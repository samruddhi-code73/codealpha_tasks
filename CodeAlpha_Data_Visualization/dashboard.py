import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('clean_amazon.csv')

os.makedirs('images/individual_charts', exist_ok=True)
os.makedirs('images/dashboard', exist_ok=True)

sns.set_style('whitegrid')

plt.rcParams['figure.figsize'] = (10, 6)

plt.figure()

sns.histplot(df['rating'], bins=20, kde=True)

plt.title('Distribution of Product Ratings',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Rating')
plt.ylabel('Count')

plt.savefig(
    'images/individual_charts/ratings_distribution.png',
    bbox_inches='tight'
)

plt.close()

plt.figure()

sns.histplot(df['discount_percentage'],
             bins=20,
             kde=True)

plt.title('Distribution of Discount Percentage',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Discount Percentage')
plt.ylabel('Count')

plt.savefig(
    'images/individual_charts/discount_distribution.png',
    bbox_inches='tight'
)

plt.close()

top_categories = (
    df['category']
    .value_counts()
    .head(10)
)

plt.figure()

top_categories.plot(kind='bar')

plt.title('Top 10 Product Categories',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Category')
plt.ylabel('Number of Products')

plt.xticks(rotation=90)

plt.savefig(
    'images/individual_charts/top_categories.png',
    bbox_inches='tight'
)

plt.close()

plt.figure()

sns.boxplot(x=df['actual_price'])

plt.title('Actual Price Outliers',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Actual Price')

plt.xlim(0, 50000)

plt.savefig(
    'images/individual_charts/price_boxplot.png',
    bbox_inches='tight'
)

plt.close()

plt.figure(figsize=(10, 6))

correlation_matrix = df[
    [
        'actual_price',
        'discounted_price',
        'discount_percentage',
        'rating',
        'rating_count'
    ]
].corr()

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap',
          fontsize=16,
          fontweight='bold')

plt.savefig(
    'images/individual_charts/heatmap.png',
    bbox_inches='tight'
)

plt.close()

plt.figure()

sns.scatterplot(
    x='actual_price',
    y='rating',
    data=df
)

plt.title('Price vs Rating',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Actual Price')
plt.ylabel('Rating')

plt.xlim(0, 50000)

plt.savefig(
    'images/individual_charts/price_vs_rating.png',
    bbox_inches='tight'
)

plt.close()

fig, axes = plt.subplots(2, 2, figsize=(18, 12))

fig.suptitle(
    'Amazon Products Visualization Dashboard',
    fontsize=22,
    fontweight='bold'
)

sns.histplot(
    df['rating'],
    bins=20,
    kde=True,
    ax=axes[0, 0]
)

axes[0, 0].set_title(
    'Ratings Distribution',
    fontsize=14,
    fontweight='bold'
)


sns.histplot(
    df['discount_percentage'],
    bins=20,
    kde=True,
    ax=axes[0, 1]
)

axes[0, 1].set_title(
    'Discount Distribution',
    fontsize=14,
    fontweight='bold'
)

top_categories.plot(
    kind='bar',
    ax=axes[1, 0]
)

axes[1, 0].set_title(
    'Top Product Categories',
    fontsize=14,
    fontweight='bold'
)

axes[1, 0].tick_params(axis='x',
                       rotation=90)

sns.boxplot(
    x=df['actual_price'],
    ax=axes[1, 1]
)

axes[1, 1].set_title(
    'Price Outliers',
    fontsize=14,
    fontweight='bold'
)

axes[1, 1].set_xlim(0, 50000)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig(
    'images/dashboard/amazon_dashboard.png',
    bbox_inches='tight'
)

plt.close()

print("All charts and dashboard saved successfully!")
