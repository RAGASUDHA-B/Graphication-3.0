import pandas as pd
import io
import matplotlib.pyplot as plt

file_path = "D:/myProjects/data_visualtion/sales_data_sample.csv"

# Open the file and preprocess it
with open(file_path, mode="r", encoding="Johab", errors="ignore") as file:
    content = file.read()

# Pass the content as a buffer to pandas
data = pd.read_csv(io.StringIO(content))
# Total sales per customer
sales_by_customer = data.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False)
sales_by_customer.head(5).plot(kind="barh", color="purple")
plt.title("Top 5 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer Name")
plt.gca().invert_yaxis()
plt.show()


