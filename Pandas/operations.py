import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#unique values
print(df["col2"].unique()) #unique elements in col 2 by unique
print(len(df["col2"].unique())) #amount of unique elements in col 2 by len
print(df["col2"].nunique()) #amount of unique elements in col 2 by nunique
print(df["col2"].value_counts()) #counts frequency of each iteam in col 2

#selecting data 
sel_val_df_1 = df[df["col1"]>2] #select value in col1 grater than 2
print(sel_val_df_1)

sel_val_df_2 = df[(df["col1"]>2) & (df["col2"]==666)] #select value in col1 & col2 condition
print(sel_val_df_2)

#apply function 

df_sum = df['col1'].sum() #apply buildin function
print(df_sum)


def times2 (x):
    return x*2

df_times2 = df["col1"].apply(times2) #apply custom function for df
print(df_times2)

df_times3 = df["col1"].apply(lambda x: x*3)#apply custom lambda function for df
print(df_times3)

#useful operations

print(df.columns)
print(df.index)

df.drop("col1", axis=1) 
print(df)

del df["col1"] #Removing a Column
print(df)

df = df.sort_values("col2") #sort from smaler to grater 
print(df)

df = df.isnull() #define if null exist 
print(df)

#initial new df and use pivot function
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

new_df = pd.DataFrame(data)
new_df = new_df.pivot_table(values='D',index=['A', 'B'])
print(new_df)









