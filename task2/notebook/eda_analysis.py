import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset from Task 1
df = pd.read_csv('../../task1/output/cleaned_sales_data.csv')

# Display first 5 rows
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Sales distribution graph
plt.figure(figsize=(8,5))
sns.histplot(df['sales'], bins=20)

plt.title('Sales Distribution')

# Save graph
plt.savefig('../vizualization/sales_distribution.png')

print("\nEDA Completed Successfully!")
# Top 10 countries by sales

top_countries = df.groupby('country')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')

plt.title('Top 10 Countries by Sales')
plt.xlabel('Country')
plt.ylabel('Sales')

plt.tight_layout()

plt.savefig('../vizualization/top_countries_sales.png')

print("Top countries graph created!")
# Correlation heatmap

numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10,6))

sns.heatmap(numeric_df.corr(), annot=True)

plt.title('Correlation Heatmap')

plt.savefig('../vizualization/correlation_heatmap.png')

print("Correlation heatmap created!")