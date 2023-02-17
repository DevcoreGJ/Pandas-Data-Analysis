# Import necessary libraries
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Group data by category and compute mean of each group
grouped_data = data.groupby('category').mean()

# Print the grouped data
print(grouped_data)

# Compute summary statistics for the entire dataset
print(data.describe())

# Merge data with another DataFrame on column_name
data2 = pd.DataFrame({'column_name': ['Column 1', 'Column 2', 'Column 3'],
                      'new_column': [1, 2, 3]})
merged_data = pd.merge(data, data2, on='column_name')

# Print the merged data
print(merged_data)

