import pandas as pd
from sklearn.preprocessing import StandardScaler

# Dataset 1
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Age': [20, None, 25]
})

# Dataset 2 (for integration)
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Salary': [20000, 30000, None]
})

# 🔹 Data Integration (merge datasets)
df = pd.merge(df1, df2, on='ID')

print("After Integration:\n", df)

# 🔹 Handling Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# 🔹 Data Transformation (new feature)
df['Age_Salary_Ratio'] = df['Age'] / df['Salary']

# 🔹 Feature Scaling
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nFinal Processed Data:\n", df)