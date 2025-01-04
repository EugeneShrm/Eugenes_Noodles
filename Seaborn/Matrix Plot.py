import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp

tips = sns.load_dataset("tips") #seaborn buildin dataset 
flights = sns.load_dataset("flights") #seaborn buildin dataset 
print(tips.head())
print(flights.head())

# Calculate the correlation matrix for numeric columns in the tips dataset
tips_corr = tips.select_dtypes(include='number').corr()
print(tips_corr)

#pivot table for flights 
pt_flights = flights.pivot_table(index="month", columns="year", values="passengers")
print(pt_flights)

#heatmap
heat_map_tips = sns.heatmap(tips_corr, linecolor="white", linewidths=2)
heat_map_flights = sns.heatmap(pt_flights, cmap = "coolwarm")
# plt.show()

#clustermap
cluster_map_tips = sns.clustermap(tips_corr)
clustert_map_flights = sns.clustermap(pt_flights, cmap="coolwarm", standard_scale=1)
plt.show()

