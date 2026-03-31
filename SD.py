import math

# Input values and frequencies
x = [10, 20, 30, 40, 50]      # discrete values
f = [3, 7, 5, 2, 3]           # corresponding frequencies

# Step 1: Calculate total frequency
N = sum(f)

# Step 2: Calculate mean
mean = sum(x[i] * f[i] for i in range(len(x))) / N

# Step 3: Calculate variance
variance = sum(f[i] * (x[i] - mean) ** 2 for i in range(len(x))) / N

# Step 4: Standard deviation
std_dev = math.sqrt(variance)

# Output
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)