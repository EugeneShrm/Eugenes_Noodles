import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

linear_plot = sns.lmplot(x="total_bill", y="tip", data=tips, col = "sex", row="time")
plt.show()