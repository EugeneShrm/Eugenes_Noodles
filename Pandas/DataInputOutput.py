import numpy as np
import pandas as pd

#read file CSV, JSON, HTML, etc
read_csv = pd.read_csv("example")
print(read_csv)

#create file 
My_output = read_csv.to_csv("My_output", index=False) # False is needed to skip the index, as it is already exist
print(My_output)

#read excel
read_excel = pd.read_excel("Excel_Sample.xlsx", sheet_name='Sheet1') #sheet_name need to choose sheet/tab
print(read_excel)

#create excel
My_excel = read_excel.to_excel("My_Excel_Sample.xlsx", sheet_name='Sheet2', index=False)
print(My_excel)

#read HTML, using for webscraping
read_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
type(read_html) #output: list, and each item is df
print(read_html)
print(read_html[0].head()) #choose first item of html 

#read SQL
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:') # Create an in-memory SQLite database

# Write the DataFrame from CSV to the SQL database
read_csv = pd.read_csv("example") #import data from CSV file 
read_csv.to_sql('data', engine, index=False, if_exists='replace')

# Read the data back from the SQL database
sql_df = pd.read_sql('SELECT * FROM data', con=engine)
print(sql_df)


