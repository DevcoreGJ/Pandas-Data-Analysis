# Import necessary libraries
import pandas as pd
import numpy as np

# Load data from CSV file
data = pd.read_csv('data.csv')

# Display first 5 rows of the data
print(data.head())

# Get basic statistics of the data
print(data.describe())

# Group data by a categorical variable
grouped_data = data.groupby('category').mean()
print(grouped_data)

# Merge two dataframes by a common column
merged_data = pd.merge(data1, data2, on='column_name')

# Reshape data using pivot tables
pivot_table = pd.pivot_table(data, values='value', index=['index_column'], columns=['column_name'], aggfunc=np.sum)

# Filter data using boolean indexing
filtered_data = data[data['column_name'] > 10]

# Drop missing values from the data
cleaned_data = data.dropna()

# Plot data using matplotlib
import matplotlib.pyplot as plt
plt.plot(data['column_name'], data['value'])
plt.title('Title of the plot')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()
