import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Load data
df = pd.read_csv("data.csv")

# Line Chart
plt.plot(df['Category'], df['Value'], marker='o')
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(df['Category'], df['Value'])
plt.title("Bar Chart")
plt.show()

# Tree Map
squarify.plot(sizes=df['Value'], label=df['Category'])
plt.title("Tree Map")
plt.axis('off')
plt.show()