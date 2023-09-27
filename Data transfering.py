import csv
import pandas as pd


salesData = pd.read_csv("daily_sales_data_0.csv")
salesData = salesData.drop(
    labels=[x for x in range(1,13720) if (x%28 not in [0,1,2,3])],
    axis = 0
    )

salesData.to_csv("daily_sales_data.csv", index=False, header = True)

def transferData(fileName):
    salesData = pd.read_csv(fileName)
    salesData = salesData.drop(
    labels=[x for x in range(1,13720) if (x%28 not in [0,1,2,3])],
    axis = 0
    )
    
    salesData.to_csv("daily_sales_data.csv", mode = "a", index=False, header = False)

for fileName in ["daily_sales_data_1.csv", "daily_sales_data_2.csv"]:
    transferData(fileName)

#everything up to here transfers only pink morsels data in new csv file

#now we want to remove the product column altogether

sales = pd.read_csv("daily_sales_data.csv")
sales = sales.drop( labels = ["product"], axis = 1)

sales["price"] = sales["price"].str[1:]

sales["price"] = sales["price"].astype(float)

sales["sales"] = sales["quantity"] * sales["price"]

finalData = sales[["sales", "date", "region"]]

finalData.to_csv("daily_sales_data.csv", index = False , header = True)

print(finalData)
