import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

file_path = "D:/myProjects/data_visualtion/sales_data_sample.csv"
with open(file_path, mode="r", encoding="Johab", errors="ignore") as file:
    content = file.read()
data = pd.read_csv(io.StringIO(content))

def categorize_customer(name):
    if "Gift" in name or "Toys" in name or "Collectables" in name:
        return "Gift Stores"
    elif "Corporate" in name or "Technics" in name:
        return "Corporate Buyers"
    else:
        return "General Stores"

data['CHANNEL_TYPE'] = data['CUSTOMERNAME'].apply(categorize_customer)

channel_sales = data.groupby('CHANNEL_TYPE')['SALES'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
channel_sales.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Sales Distribution by Customer Channels')
plt.ylabel('')  
plt.tight_layout()
plt.show()

customer_orders = data['CUSTOMERNAME'].value_counts()
print(customer_orders)  
def categorize_customer(order_count):
    if order_count == 1:
        return "One-time Customers"
    elif 2 <= order_count <= 5:
        return "Repeat Customers (2-5 Orders)"
    else:
        return "Loyal Customers (6+ Orders)"

customer_categories = customer_orders.apply(categorize_customer)

print(customer_categories.value_counts())
customer_category_counts = customer_categories.value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=customer_category_counts.index, y=customer_category_counts.values, palette='viridis')
plt.title('Customer Categories: One-time vs Repeat vs Loyal Customers')
plt.xlabel('Customer Category')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()
