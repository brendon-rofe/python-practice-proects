import pandas as pd
import matplotlib.pyplot as plt

file_path = 'ecom_inv_mgmnt\inventory_sales_data.csv'
data = pd.read_csv(file_path)

print(data.head())

print(data.isnull().sum())

data['Date'] = pd.to_datetime(data['Date'])  # Converting Date column to datetime
daily_sales = data.groupby('Date')['Quantity_Sold'].sum()
plt.figure(figsize=(12, 6))
plt.plot(daily_sales)
plt.title('Total Sales per Day')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.show()
