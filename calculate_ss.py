import pandas as pd
from scipy.stats import norm

# Load the data from the newly uploaded snippet Excel file
# file_path = './test_ab.xlsx'
file_path = './test_ab35.xlsx'
df = pd.read_excel(file_path, sheet_name='test_ab', usecols=['group', 'revenue'])

# Calculate the avgs, standard deviations, and sample sizes for each group
group_stats = df.groupby('group')['revenue'].agg(['mean', 'std', 'count'])

# Calculate avg, std deviation, and count for each group
avg_A = group_stats.loc['A', 'mean']
std_A = group_stats.loc['A', 'std']
n_A = group_stats.loc['A', 'count']

avg_B = group_stats.loc['B', 'mean']
std_B = group_stats.loc['B', 'std']
n_B = group_stats.loc['B', 'count']

# Calculate the Z-score
Z = (avg_A - avg_B) / ((std_A**2 / n_A + std_B**2 / n_B)**0.5)

# Calculate the p-value for the two-tailed test
p_value = norm.sf(abs(Z)) * 2  # sf is the survival function, equivalent to 1 - cdf

# Print results
print("Z-Score:", Z)
print("P-Value:", p_value)