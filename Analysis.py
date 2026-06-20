import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

df=pd.read_csv("Unemployment.csv")

df.dropna(inplace=True)
print(df.shape)
print(df.isnull().sum())

df.columns = df.columns.str.strip()
print(df.columns)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
print(df.head())

print("Rows:",df.shape[0])
print("Columns:",df.shape[1])

print(df.describe())

print(df['Estimated Unemployment Rate (%)'].mean())
print(df['Estimated Unemployment Rate (%)'].max())

plt.figure(figsize=(12,6))

plt.plot(
    df['Date'],
    df['Estimated Unemployment Rate (%)']
)
plt.title("Unemployment Rate over time")
plt.xlabel("Date")
plt.ylabel("Unemployement Rate (%)")
plt.show()

state_unemployment = df.groupby('Region')[
    'Estimated Unemployment Rate (%)'
].mean().sort_values(ascending=False)

print(state_unemployment)

plt.figure(figsize=(12,6))

sns.barplot(
    x=state_unemployment.values,
    y=state_unemployment.index
)

plt.title("Average Unemployment Rate by State")
plt.show()

covid_period = df[
    (df['Date'] >= '2020-03-01') &
    (df['Date'] <= '2020-12-31')
]

print(
    covid_period['Estimated Unemployment Rate (%)'].mean()
)

before_covid = df[df['Date'] < '2020-03-01']
during_covid = df[df['Date'] >= '2020-03-01']

print("Before COVID:",
      before_covid['Estimated Unemployment Rate (%)'].mean())

print("During COVID:",
      during_covid['Estimated Unemployment Rate (%)'].mean())

df['Month'] = df['Date'].dt.month_name()

monthly = df.groupby('Month')[
    'Estimated Unemployment Rate (%)'
].mean()
plt.figure(figsize=(12,6))

monthly.plot(kind='bar')

plt.title("Monthly Unemployment Trend")
plt.ylabel("Unemployment Rate (%)")

plt.show()

pivot = df.pivot_table(
    values='Estimated Unemployment Rate (%)',
    index='Region',
    columns='Area',
    aggfunc='mean'
)

plt.figure(figsize=(10,8))

sns.heatmap(
    pivot,
    annot=True,
    cmap='YlGnBu'
)

plt.title("Unemployment Heatmap")
plt.show()

fig = px.line(
    df,
    x='Date',
    y='Estimated Unemployment Rate (%)',
    color='Region',
    title='Unemployment Rate Across States'
)

fig.show()

