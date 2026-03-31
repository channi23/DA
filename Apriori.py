import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample supermarket data (one-hot encoded)
data = {
    'Milk':   [1, 0, 1, 1, 0],
    'Bread':  [1, 1, 1, 0, 1],
    'Butter': [0, 1, 1, 1, 0],
    'Jam':    [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Frequent itemsets
freq_items = apriori(df, min_support=0.4, use_colnames=True)
print("Frequent Itemsets:\n", freq_items)

# Association rules
rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)
print("\nAssociation Rules:\n", rules)
print(rules.sort_values(by='confidence', ascending=False).head(10))