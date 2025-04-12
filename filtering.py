# by using relational operator
#single condition
import pandas as pd
df=pd.read_csv("sales4.csv")
con=df["Product_Cost"]>65000
df1=df[con]
print(df1)
print()
#multiple condition
import pandas as pd
df=pd.read_csv("sales4.csv")
con=df["Product_Cost"]>50000 #1
con1=df["Product_Cost"]>60000#2
df1=df[con&con1]
print(df1)
#or
import pandas as pd
df=pd.read_csv("sales4.csv")
con=df.Product_Name == "iPhone 11"#1
con1=df.Customer_Name == "Nireekshan"#2
df1=df[con&con1]
print(df1)
# By using ILOC AND LOC
