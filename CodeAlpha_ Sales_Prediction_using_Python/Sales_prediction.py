import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("Advertising.csv")

print(df.head())
print(df.info())


print(df.isnull().sum())


plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap='Blues')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()


X = df[['TV','Radio','Newspaper']]
y = df['Sales']


X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)


model = LinearRegression()
model.fit(X_train,y_train)


y_pred = model.predict(X_test)


print("R2 Score:",r2_score(y_test,y_pred))
print("MAE:",mae:=mean_absolute_error(y_test,y_pred))
print("RMSE:",mean_squared_error(y_test,y_pred)**0.5)


plt.figure(figsize=(8,5))
plt.scatter(y_test,y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.savefig("actual_vs_prediction.png")
plt.show()


importance = pd.DataFrame({
    "Feature":X.columns,
    "Coefficient":model.coef_
})

print(importance)

plt.figure(figsize=(8,5))
sns.barplot(
    x="Coefficient",
    y="Feature",
    data=importance
)

plt.title("Advertising Impact on Sales")
plt.savefig("advertising_impact.png")
plt.show()