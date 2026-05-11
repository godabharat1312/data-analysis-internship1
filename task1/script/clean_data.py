import pandas as pd

# Load dataset
df = pd.read_csv('../dataset/sales_data_sample.csv', encoding='latin1')

# Show first rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Save cleaned dataset
df.to_csv('../output/cleaned_sales_data.csv', index=False)

print("\nData cleaning completed!")