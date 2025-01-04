import matplotlib.pyplot as plt

# Create a new figure with custom size
plt.figure(figsize=(8, 4), dpi=100)
plt.plot([1, 2, 3, 4], [10, 20, 25, 30]) # Add a plot to the figure
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Title')

plt.savefig('plot_output.pdf', format='pdf') #can be png, jpg, etc
