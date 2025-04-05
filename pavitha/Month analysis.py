
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = "D:/myProjects/data_visualtion/sales_data_sample.csv"
with open(file_path, mode="r", encoding="Johab", errors="ignore") as file:
    content = file.read()
data = pd.read_csv(io.StringIO(content))
data = pd.DataFrame({
    'CUSTOMERNAME': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie'],
    'SALES': [200, 300, 150, 150, 400],
    'QUANTITYORDERED': [2, 3, 1, 2, 4]
})

print("Original Dataset:")
print(data)

mean_data = data.groupby('CUSTOMERNAME').mean().reset_index()

median_data = data.groupby('CUSTOMERNAME').median().reset_index()

mode_data = data.groupby('CUSTOMERNAME').agg(lambda x: x.mode()[0]).reset_index()
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

# Group by month
seasonal_sales = data.groupby(data['ORDERDATE'].dt.month)['SALES'].sum()

# Line plot
plt.figure(figsize=(10, 6))
seasonal_sales.plot(kind='line', marker='o', color='purple')
plt.title('Seasonal Sales Analysis')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.tight_layout()
plt.show()

data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

data['MONTH'] = data['ORDERDATE'].dt.month

country_month_sales = data.groupby(['COUNTRY', 'MONTH'])['SALES'].sum().unstack()

countries = country_month_sales.index.tolist()
months = country_month_sales.columns.tolist()

bar_width = 0.8 / len(countries)  
positions = np.arange(len(months)) 

plt.figure(figsize=(12, 8))
for i, country in enumerate(countries):
    plt.bar(
        positions + i * bar_width, 
        country_month_sales.loc[country], 
        width=bar_width, 
        label=country
    )

plt.title('Monthly Sales by Country', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.xticks(positions + (len(countries) / 2 - 0.5) * bar_width, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.legend(title='Country', loc='upper right')
plt.tight_layout()

plt.show()
