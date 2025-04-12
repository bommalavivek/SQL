import pandas as pd
a=pd.read_csv("sales1.csv")
con=a["Customer Name"]=="Veeru"
print(a[con])
print()
import pandas as pd
a=pd.read_csv("sales1.csv")
con=a["Product"]=="Samsung m20"
print(a[con])
#iloc
import pandas as pd
df=pd.read_csv("sales2.csv")
print(df)
print()
print(df.iloc[0])
# accessing row and column
import pandas as pd
df=pd.read_csv("sales2.csv")
print(df)
print()
print(df.iloc[:,1])
print()
import pandas as pd
df=pd.read_csv("sales2.csv")
print(df)
print()
print(df.iloc[10:25,1])
#selecting multiple columns
import pandas as pd
df=pd.read_csv("sales2.csv")
print(df)
print()
print(df.iloc[0:5])
#printing two columns of the df with all rows
import pandas as pd
df=pd.read_csv("sales2.csv")
print(df)
print()
print(df.iloc[:,0:2])
#LOC
#setting index as product name
import pandas as pd
a=pd.read_csv("sales2.csv")
print(a.set_index("Product name"))
#
import pandas as pd
b=pd.read_csv("sales2.csv")
a=b.set_index("Product name")
print(a.loc["iPhone 9"])
#
import pandas as pd
df1=pd.read_csv("sales2.csv")
df1.set_index("Product name",inplace=True)
a=["iPhone 9","ThinkPad Laptop"]
b=["Product cost","Customer id"]
df2=df1.loc[a,b]
print(df2)