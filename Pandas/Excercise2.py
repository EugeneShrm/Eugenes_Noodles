import pandas as pd

# Use the absolute path to the CSV file
df = pd.read_csv("Ecommerce Purchases")
print(df.head(5))

print(df.info()) # How many rows and columns are there?
print(df["Purchase Price"].mean()) # What is the average Purchase Price?
print(df[df["Purchase Price"] == df["Purchase Price"].min()]) # Get the row with the minimum "Purchase Price"
print(df[df["Purchase Price"] == df["Purchase Price"].max()]) # Get the row with the maximum "Purchase Price"
print(df["Language"] == "en") #How many people have English 'en' as their Language of choice on the website?
print(sum(df["Job"] == "Lawyer")) #How many people have the job title of "Lawyer" ? 
print(df["Job"].value_counts().head(5)) #What are the 5 most common Job Titles?
print(df['AM or PM'].value_counts()) #How many people made the purchase during the AM and how many people made the purchase during PM ? 
print(df[df["Lot"] == "90 WT"]["Purchase Price"]) #Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print(df[df["Credit Card"] == 4926535242672853]["Email"]) # What is the email of the person with the following Credit Card Number: 4926535242672853 
print(df[(df["CC Provider"] == "American Express") & (df["Purchase Price"] > 95)].count()) #How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print(sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25'))#How many people have a credit card that expires in 2025?
print(df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)