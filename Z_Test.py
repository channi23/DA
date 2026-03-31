import numpy as np
from statsmodels.stats.weightstats import ztest

# Sample data
data1 = np.array([45, 50, 47, 52, 48, 49, 51, 46, 53, 50])
data2 = np.array([49, 51, 46, 53, 50, 48, 47, 52, 49, 50])

# 🔹 Z-test for Single Mean
z1, p1 = ztest(data1, value=50)
print("Single Mean Z-test:")
print("Z =", z1, "P =", p1)

# 🔹 Z-test for Difference of Means
z2, p2 = ztest(data1, data2)
print("\nDifference of Means Z-test:")
print("Z =", z2, "P =", p2)