# Import necessary libraries
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "D:/myProjects/data_visualtion/sales_data_sample.csv"
with open(file_path, mode="r", encoding="Johab", errors="ignore") as file:
    content = file.read()
data = pd.read_csv(io.StringIO(content))
print("data")


data['REVENUE_WITH_DISCOUNT'] = data['QUANTITYORDERED'] * data['PRICEEACH']

data['REVENUE_WITHOUT_DISCOUNT'] = data['QUANTITYORDERED'] * data['MSRP']


data['DISCOUNT'] = ((data['MSRP'] - data['PRICEEACH']) / data['MSRP'].replace(0, 1)) * 100

data['DISCOUNT_RANGE'] = pd.cut(data['DISCOUNT'], bins=[0, 10, 20, 30, 40, 50, 100], 
                                labels=['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50+%'])

revenue_comparison = data.groupby('DISCOUNT_RANGE').sum()[['REVENUE_WITH_DISCOUNT', 'REVENUE_WITHOUT_DISCOUNT']]


plt.figure(figsize=(12, 6))
revenue_comparison.plot(kind='bar', color=['coral', 'skyblue'], width=0.8)
plt.title('Revenue: With Discounts vs Without Discounts')
plt.xlabel('Discount Range (%)')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend(['With Discounts', 'Without Discounts'], loc='upper right')
plt.tight_layout()
plt.show()

revenue_by_discount = data.groupby('DISCOUNT_RANGE')['REVENUE_WITH_DISCOUNT'].sum()

plt.figure(figsize=(10, 6))
revenue_by_discount.plot(kind='bar', color='coral')
plt.title('Revenue vs Discount Range (With Discounts)')
plt.xlabel('Discount Range (%)')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

max_revenue_range = revenue_by_discount.idxmax()
max_revenue = revenue_by_discount.max()           

print(f"The optimal discount range is '{max_revenue_range}' with total revenue: {max_revenue}")
