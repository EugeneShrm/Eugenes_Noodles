import pandas as pd

df = pd.read_csv("Salaries.csv") #import CSV
print(df)
print(df.head()) #print the first 5 rows of the DataFrame
print(df.info()) #output RangeIndex: 148654 entries
print(df["BasePay"].mean()) #What is the average BasePay? 
print(df["OvertimePay"].max()) #What is the highest amount of OvertimePay in the dataset?
print(df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']) #What is the job title of JOSEPH DRISCOLL ? 
print(df[df["TotalPayBenefits"] == df["TotalPayBenefits"].max()]) #What is the name of highest paid person (including benefits)?
print(df.iloc[df["TotalPayBenefits"].idxmax()]) # v2 for highest paid person 
print(df[df["TotalPayBenefits"] == df["TotalPayBenefits"].min()]) #What is the name of lowest paid person (including benefits)?
print(df.iloc[df["TotalPayBenefits"].argmin()]) #V2 for lowest paid person
print(df.groupby('Year')['BasePay'].mean()) #What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print(df['JobTitle'].nunique()) #How many unique job titles are there?
print(df['JobTitle'].value_counts().head(5)) #What are the top 5 most common jobs?
print(sum(df[df['Year']==2013]['JobTitle'].value_counts() == 1)) #How many Job Titles were represented by only one person in 2013? 

#How many people have the word Chief in their job title?
#v1
# Count occurrences of the word "Chief" in the JobTitle column (case insensitive)
chief_count = df['JobTitle'].str.contains('Chief', case=False, na=False).sum()
# Print the result
print(f"Number of people with 'Chief' in their job title: {chief_count}")

#v2
# Define a function that checks if the word 'chief' is present in the job title
def chief_string(job_title):
    if 'chief' in job_title.lower():
        return True # Return True if 'chief' is found
    else:
        return False 
# The 'apply' method applies the function to each row of the column
# The lambda function passes each job title (x) to the 'chief_string' function
print(sum(df['JobTitle'].apply(lambda x: chief_string(x))))