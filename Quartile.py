import numpy as np

# Discrete values and frequencies
x = [10, 20, 30, 40, 50]
f = [3, 7, 5, 2, 3]

# Step 1: Expand data
data = []
for i in range(len(x)):
    data.extend([x[i]] * f[i])

# Convert to numpy array
data = np.array(data)

# Step 2: Calculate quartiles
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

# Step 3: Quartile Deviation
QD = (Q3 - Q1) / 2

# Output
print("Q1 =", Q1)
print("Q3 =", Q3)
print("Quartile Deviation =", QD)