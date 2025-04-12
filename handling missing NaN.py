import pandas as pd
df=pd.read_csv("fruits1.csv")
print(df)
#isna()   we are using in real time true or false
import pandas as pd
df=pd.read_csv("fruits1.csv")
print(df)
print()
print(df.isna())
#isna().sum  it will count number of NaN 
import pandas as pd
df=pd.read_csv("fruits1.csv")
print(df)
print()
print(df.isna().sum())
#dropna()   In this it will remove the  NaN 
import pandas as pd
df=pd.read_csv("fruits1.csv")
print(df)
print()
print(df.dropna())
#astype   It will conver float into int
import pandas as pd
df=pd.read_csv("fruits1.csv")
df1=df.dropna()
df2=df1.astype(int)
print(df1.head())
print()
print(df2.head())
#df.fillna()  This method will fill NaN with zero or with number
import pandas as pd
df=pd.read_csv("fruits1.csv")
print(df)
df1=df.fillna(64)
print(df1)