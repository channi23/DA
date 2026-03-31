import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset with missing values
data = {
    'Age': [20, 25, None, 30, 35],
    'Salary': [20000, 25000, 30000, None, 50000]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Handling missing values (fill with mean)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Feature Scaling
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nProcessed Data:\n", df)