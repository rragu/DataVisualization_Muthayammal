## Install Libraries
import matplotlib.pyplot as plt
import numpy as np

## Generate exmaple data
x = np.linspace(0, 10, 100)
y = np.sin(x)

## Plot the data
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

## Save the plot to the file(optional)
plt.savefig('plot.png')

## Show the plot (Optional)
# plt.show()