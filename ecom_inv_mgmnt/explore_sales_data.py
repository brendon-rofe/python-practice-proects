import pandas as pd
import matplotlib.pyplot as plt

file_path = 'ecom_inv_mgmnt\inventory_sales_data.csv'
data = pd.read_csv(file_path)

print(data.head())