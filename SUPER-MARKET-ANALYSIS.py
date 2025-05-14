# Supermarket Sales Analysis using Pandas, Matplotlib, and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set seaborn style
sns.set(style='whitegrid')

# Load dataset
df = pd.read_csv('supermarket_sales.csv')

# Display basic info
print("First 5 rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Convert Date and Time
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'],format='%H:%M').dt.time
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour


# 1. Peak Sales Hours
plt.figure(figsize=(10, 6))
sns.histplot(df['Hour'], bins=24, kde=False)
plt.title("Sales Volume by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Sales")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# 2. Best Performing Branches
branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 3. Payment Method Popularity
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Payment', order=df['Payment'].value_counts().index)
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.show()

# 4. Product Line Profitability
product_sales = df.groupby('Product line')['Total'].sum().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title("Total Sales by Product Line")
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.tight_layout()
plt.show()

