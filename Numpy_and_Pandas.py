import numpy as np
import pandas as pd

# Creating NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Standard Deviation:", np.std(arr))

# Creating Pandas DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [85, 90, 78, 92],
    'Age': [20, 21, 19, 22]
}

df = pd.DataFrame(data)

print("\nDataFrame:\n", df)

# Basic operations
print("\nFirst 2 rows:\n", df.head(2))
print("\nColumn Names:", df.columns)
print("\nMean Marks:", df['Marks'].mean())
print("\nMax Marks:", df['Marks'].max())

# Filtering
print("\nStudents with Marks > 80:\n", df[df['Marks'] > 80])