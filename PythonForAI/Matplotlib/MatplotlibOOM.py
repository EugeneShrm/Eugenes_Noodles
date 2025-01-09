import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 5)
y = x ** 2

#Object Oriented Method insdead of plot function 
fig = plt.figure() # Creates blank canvas

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.4]) # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b--')
axes1.set_xlabel('X_label_axes1')
axes1.set_ylabel('Y_label_axes1')
axes1.set_title('Axes 1 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')
plt.show()