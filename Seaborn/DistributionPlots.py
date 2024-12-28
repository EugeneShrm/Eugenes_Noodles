import numpy as np
import seaborn as sns

tips = sns.load_dataset("tips") #seaborn buildin dataset 
print(tips)
print(sns.displot(tips["total_bill"])) #use displot type

