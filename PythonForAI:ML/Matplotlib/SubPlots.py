import matplotlib.pyplot as plt

# #V1
# Define data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# # Create a figure with 1 row and 2 columns of subplots
fig, axes = plt.subplots(figsize=(8, 4), nrows=1, ncols=2)

# # Iterate over the array of axes and add plots
for ax in axes:
    ax.plot(x, y, 'b')           # Plot x vs. y in blue
    ax.set_xlabel('x')           # Set x-axis label
    ax.set_ylabel('y')           # Set y-axis label
    ax.set_title('Sample Plot')  # Set title

plt.show() # Display the figure

#v2
fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title("First")

axes[1].plot(x,y)
axes[1].set_title("Second")
plt.show()
