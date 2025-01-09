import matplotlib.pyplot as plt

# Define data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
y2 = [0, 2, 8, 18, 32]  # Second line data (just double the original y values)

# Plot two lines
plt.plot(x, y, label='Line 1')
plt.plot(x, y2, label='Line 2')  # Use the predefined second line data

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Two Lines Plot')

# Display the legend
plt.legend(loc=2) #location code for legend

# Show the plot
plt.show()

