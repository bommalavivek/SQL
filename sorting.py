import pandas as pd
a=pd.read_csv("sales4.csv")
b=a.sort_values(by="Product_Cost")
print(b)