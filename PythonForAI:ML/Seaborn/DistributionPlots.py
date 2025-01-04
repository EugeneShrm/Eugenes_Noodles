import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips") #seaborn buildin dataset 
print(tips)

#displot
total_bill = sns.displot(tips["total_bill"], kde=True, bins=20) # add kde and bins
# Adjust the x and y axes limits
total_bill.ax.set_xlim(0, 50)  # Set x-axis range
total_bill.ax.set_ylim(0, 100) 
plt.show()

#joinplot
tips = sns.load_dataset("tips")
joint_plot = sns.jointplot(x="total_bill", y="tip", data=tips, kind = "hex") # kind = hex/reg/kde
plt.show()

#pair plot
pair_plot = sns.pairplot(tips, hue = "sex", palette="coolwarm")
plt.show()

#rug plot
rug_plot = sns.rugplot(tips["total_bill"])
plt.show()


