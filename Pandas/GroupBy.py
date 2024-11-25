import numpy as np
import pandas as pd

# Create dataframe
data = {'Company':['GOOG','MSFT','MSFT','FB','FB', 'GOOG'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

# groupby column name
by_company = df.groupby("Company") #Group by 'Company'
print(by_company) #it just shows grouped by object is created

#v1
by_company_sum = by_company["Sales"].mean()
print(by_company_sum)

#v2
by_company_sum = by_company.sum() # it can sum str
print(by_company_sum)

#Comprehensive variant 
data = {'Company':['GOOG','MSFT','MSFT','FB','FB', 'GOOG'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)

#groupby and reach FB
by_company_sum = df.drop(columns="Person").groupby("Company").sum().loc["FB"] #show just Sales for FB
print(by_company_sum)

#describe the entity
by_company_sum_describe = df.groupby("Company").describe()
print(by_company_sum_describe)
