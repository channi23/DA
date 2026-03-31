from scipy import stats

# Sample data (3 groups)
group1 = [45, 50, 47, 52]
group2 = [48, 49, 51, 50]
group3 = [60, 62, 61, 59]

# One-Way ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3)

print("F-Statistic:", f_stat)
print("P-Value:", p_val)