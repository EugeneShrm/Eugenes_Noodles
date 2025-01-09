import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_csv('df3')
print(df3)

#ex1
# Create a scatter plot from the DataFrame `df3`
df3.plot.scatter(
    x='a',          # Column 'a' is used for the x-axis
    y='b',          # Column 'b' is used for the y-axis
    c='red',        # Points are colored red
    s=50,           # Size of each scatter point is set to 50
    figsize=(12, 3) # The figure size is set to 12 units wide and 3 units tall
)

# Display the plot
plt.show()

#ex2
plt.style.use('ggplot')
df3['a'].plot.hist(alpha=0.5,bins=25)
plt.show()

#ex3
df3.plot.box(x= "a", y = "b")
plt.show()
