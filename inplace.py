import pandas as pd
a=pd.read_csv("sales3.csv")
z={
    "ord id":"order_Id",
    "cust name":"customer_name",
    "cust id":"customer_id",
    "prod name":"product_name",
    "prod cost":"product_cost"
}
b=a.rename(columns=z,inplace=True)
print(a.head())
print()
print(a.head())
print()
import pandas as pd
df=pd.read_csv("sales1.csv")          
print(df)
print()
print(df.isna()) # if we have null values in the dataset then for that NaN it will show as True