import numpy as np
import matplotlib.pyplot as plt


x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Create subplots with 1 row and 2 columns
fig, axes = plt.subplots(figsize=(14, 8),nrows=1, ncols=1)

# MATLAB style line color and style for the first subplot
axes.plot(x, y, 'b.-')  # blue line with dots
axes.set_title("Title")

# Green dashed line for the second subplot (y + y)
axes.plot(x, np.array(y) + np.array(y), 'g--')  # green dashed line

# Green dashed line for the second subplot (y + y)
axes.plot(x, np.array(y) + np.array(y) + np.array(y), color = "Purple", linewidth=5, marker="o", markersize=20, markerfacecolor= "b")  # purple line with different stuff 

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
axes.plot(x+np.array(2), y, color="green", lw=3, linestyle='-')
axes.plot(x+np.array(3), y, color="green", lw=3, ls='-.')
axes.plot(x+np.array(4), y, color="green", lw=3, ls=':')


# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
axes.plot(x+np.array(5), y, lw=3, ls='-', marker='+')
axes.plot(x+np.array(6), y, color="blue", lw=3, ls='--', marker='o')
axes.plot(x+np.array(7), y, color="blue", lw=3, ls='-', marker='s')
axes.plot(x+np.array(8), y, color="blue", lw=3, ls='--', marker='1')

# marker size and color
axes.plot(x+np.array(9), y, color="purple", lw=1, ls='-', marker='o', markersize=2)
axes.plot(x+np.array(10), y, color="purple", lw=1, ls='-', marker='o', markersize=4)
axes.plot(x+np.array(11), y, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
axes.plot(x+np.array(12), y, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");
plt.show()


