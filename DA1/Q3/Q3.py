import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv('Q3\juice_stall_transactions.csv')

frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules:\n",rules)

print("\n\n21BBS0207")