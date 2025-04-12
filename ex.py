import pandas as pd
df=pd.read_csv("sales1.csv")
print(df)
print(df.values)
import pandas as pd
details=[
    ["vivek",20,20000],
    ["nikhil",40,65000],
    ["Throshitha",24,100000]
]
a=["name","age","salary"]
df=pd.DataFrame(details,columns=a)
print(df.T) 
