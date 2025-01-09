import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp

iris = sns.load_dataset("iris")
print(iris)

#pair grid plot 
pair_plot = sns.PairGrid(iris.head(10))
plt.show(iris)

#face grid 
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")
plt.show(iris)
