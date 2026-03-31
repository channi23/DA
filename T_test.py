from scipy import stats

# Sample data
data1 = [45, 50, 47, 52, 48]
data2 = [49, 51, 46, 53, 50]

# 🔹 One-Sample T-Test
t1, p1 = stats.ttest_1samp(data1, 50)
print("One-Sample T-Test:")
print("T =", t1, "P =", p1)

# 🔹 Independent T-Test
t2, p2 = stats.ttest_ind(data1, data2)
print("\nIndependent T-Test:")
print("T =", t2, "P =", p2)