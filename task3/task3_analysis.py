import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_sales_data.csv", encoding="latin1")

# Convert ORDERDATE into date format
df["orderdate"] = pd.to_datetime(df["orderdate"])

# Display first five rows
print(df.head())
# -------------------------------
# KPI Calculations
# -------------------------------

# Total Sales
total_sales = df["sales"].sum()

# Total Orders
total_orders = df["ordernumber"].nunique()

# Total Customers
total_customers = df["customername"].nunique()

# Total Quantity Sold
total_quantity = df["quantityordered"].sum()

# Average Order Value
average_order_value = total_sales / total_orders

# Display KPIs
print("\n------ KPI REPORT ------")
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: {average_order_value:.2f}")
# -------------------------------
# Sales by Product Line
# -------------------------------

sales_by_product = df.groupby("productline")["sales"].sum().sort_values(ascending=False)

print("\n------ Sales by Product Line ------")
print(sales_by_product)
plt.figure(figsize=(10,6))
sales_by_product.plot(kind="bar")

plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# -------------------------------
# Sales by Country
# -------------------------------

sales_by_country = df.groupby("country")["sales"].sum().sort_values(ascending=False)

print("\n------ Sales by Country ------")
print(sales_by_country)

plt.figure(figsize=(12,6))
sales_by_country.plot(kind="bar")

plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# -------------------------------
# Monthly Sales Trend
# -------------------------------

monthly_sales = df.groupby(df["orderdate"].dt.to_period("M"))["sales"].sum()

print("\n------ Monthly Sales ------")
print(monthly_sales)

monthly_sales.plot(figsize=(12,6), marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()