import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Set x values from 0 to 2*pi for one full period of the sine wave
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

num_frames = 100
def update(frame):
    x_pos = x[int(frame) % len(x)]
    y_pos = y[int(frame) % len(x)]
    plt.cla()
    plt.scatter(x_pos, y_pos, s=100)
    plt.xlim(0, 2*np.pi)
    plt.ylim(-2, 2)

fig, ax = plt.subplots()

# Setting the interval to 50ms means the animation will update every 50 milliseconds
animation = FuncAnimation(fig, update, frames=num_frames, interval=50)  

# To save the animation as a GIF, you need to have the 'imagemagick' package installed
# animation.save('ball_animation.gif', writer='imagemagick')

plt.show()
