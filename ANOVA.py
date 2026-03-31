import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# -------- One-Way ANOVA --------
group1 = [45, 50, 47, 52]
group2 = [48, 49, 51, 50]
group3 = [60, 62, 61, 59]

f1, p1 = stats.f_oneway(group1, group2, group3)
print("One-Way ANOVA:")
print("F =", f1, "P =", p1)

# -------- Two-Way ANOVA --------
data = {
    'Score': [85, 90, 88, 92, 95, 89],
    'Method': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Gender': ['M', 'F', 'M', 'F', 'F', 'M']
}

df = pd.DataFrame(data)

model = ols('Score ~ Method + Gender + Method:Gender', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("\nTwo-Way ANOVA:\n", anova_table)