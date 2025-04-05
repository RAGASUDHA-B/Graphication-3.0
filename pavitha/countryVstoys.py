import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "D:/myProjects/data_visualtion/sales_data_sample.csv"

with open(file_path, mode="r", encoding="Johab", errors="ignore") as file:
    content = file.read()
data = pd.read_csv(io.StringIO(content))

toys_within_countries = data.groupby(['COUNTRY', 'PRODUCTLINE'])['QUANTITYORDERED'].sum()

most_sold_in_countries = toys_within_countries.groupby('COUNTRY').idxmax() 
most_sold_quantities = toys_within_countries.groupby('COUNTRY').max()  
most_sold = pd.DataFrame({
    'Most Sold Product Line': most_sold_in_countries,
    'Quantity Sold': most_sold_quantities
})

most_sold.reset_index(inplace=True)
print(most_sold)

plt.figure(figsize=(12, 8))
sns.barplot(data=most_sold, x='COUNTRY', y='Quantity Sold', hue='Most Sold Product Line', dodge=False)
plt.title('Most Sold Toys by Product Line in Each Country')
plt.xlabel('Country')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.legend(title='Product Line')
plt.tight_layout()
plt.show()


total_quantity_by_country = data.groupby('COUNTRY')['QUANTITYORDERED'].sum().sort_values(ascending=False)

top_5_countries = total_quantity_by_country.head(5).index


filtered_data = data[data['COUNTRY'].isin(top_5_countries)]

top_countries_toys = filtered_data.groupby(['COUNTRY', 'PRODUCTLINE'])['QUANTITYORDERED'].sum().unstack()

plt.figure(figsize=(12, 8))
top_countries_toys.plot(kind='bar', stacked=True, cmap='Set2')
plt.title('Top 5 Countries: Toys Sold by Product Line')
plt.xlabel('Country')
plt.ylabel('Total Quantity Ordered')
plt.xticks(rotation=45)
plt.legend(title='Product Line', loc='upper right', bbox_to_anchor=(1.25, 1))
plt.tight_layout()
plt.show()



