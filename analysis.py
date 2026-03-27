import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales.csv")

# Create total column
df["total"] = df["price"] * df["quantity"]

# Total revenue
total_revenue = df["total"].sum()
print("Total Revenue:", total_revenue)

# Top products
top_products = df.groupby("product")["total"].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

# Sales by month
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

sales_by_month = df.groupby("month")["total"].sum()
print("\nSales by Month:\n", sales_by_month)

# Plot
sales_by_month.plot(kind="bar")
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.show()

# Top customers
top_customers = df.groupby("customer")["total"].sum().sort_values(ascending=False)
print("\nTop Customers:\n", top_customers)