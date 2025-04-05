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
print(data.columns)

