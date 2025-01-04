import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips") #seaborn buildin dataset 
tips = tips.head()
print(tips)

#cat 
# plot is the most general form of a categorical plot. It can take in a kind parameter to adjust the plot type
cat_plot = sns.catplot(x='sex',y='total_bill',data=tips,kind='bar') #can make bar, violing, etc
plt.show()

#bar plot - numerical vs categorical data 
bar_plot = sns.barplot(x="sex", y= "total_bill", data=tips, palette="coolwarm")
plt.show()

#count plot
count_plot = sns.countplot(x="sex", data = tips) #the same and pd.count
"""sex_count = tips["sex"].count()
print(sex_count)"""
plt.show()

#box plot 
box_plot= sns.boxplot(x="day", y="total_bill", data=tips, hue = "smoker", palette='rainbow')
plt.show()

#violing plot
violing_plot = sns.violinplot(x="day", y="total_bill", data=tips, hue = "sex", split=True)
plt.show()

#strip plot
strip_plot = sns.stripplot(x="day", y="total_bill", data=tips,jitter=True) #jitter adding mess when there are a lot of dots 
plt.show()

#swarm plot - combination of strip plot and violing plot 
swarm_plot = sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)
plt.show()