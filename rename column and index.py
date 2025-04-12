#changing one column name
import pandas as pd
a=pd.read_csv("sales3.csv")
z={
    "ord id":"order Id"
}
b=a.rename(columns=z)
print(a.head())
print()
print(b.head())
#changing two column name
import pandas as pd
a=pd.read_csv("sales3.csv")
z={
    "ord id":"order Id",
    "cust name":"Customer name"
}
b=a.rename(columns=z)
print(a.head())
print()
print(b.head())
#changing more than two column name
import pandas as pd
a=pd.read_csv("sales3.csv")
z={
    "ord id":"order_Id",
    "cust name":"customer_name",
    "cust id":"customer_id",
    "prod name":"product_name",
    "prod cost":"product_cost"
}
b=a.rename(columns=z)
print(a.head())
print()
print(b.head())
#chaning index in datafrma
import pandas as pd
d={
    "order_id":[1,2,3],
    "customer_name":["vivek","vijay","mani"],
    "product":["iphone","htc","mac"]
}
i={
    0:10,
    1:20,
    2:30
}
df=pd.DataFrame(d)
df1=df.rename(index=i)
print(df)
print()
print(df1)