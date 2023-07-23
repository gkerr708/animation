import numpy as np, matplotlib.pyplot as plt, random
from matplotlib.animation import FuncAnimation 


fps = 144
x_data = np.linspace(0,100,100)
y_data = x_data
for x, y in zip(x_data, y_data):
    plt.clf()
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.scatter(x,y, color='blue')
    plt.pause(1/fps)
plt.show()




