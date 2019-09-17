from time import time 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np 
from environment import Environment

def math_function(x, y=0):
    # return 100 * np.sqrt(np.abs(y - (0.01 * x**2))) + 0.01*np.abs(x + 10)
    return -(y + 47) * np.sin(np.sqrt(np.abs(y + x/2 + 47))) - x*np.sin(np.sqrt(np.abs(x-(y+47))))

def plot_function():
    scale = 10
    x = np.arange(-512, 512, scale)
    y = np.arange(-512, 512, scale)
    x, y = np.meshgrid(x, y)
    z = math_function(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, antialiased=False)
    plt.show()

    # bx = fig.add_subplot(111, projection='3d')
    # bx.scatter(env.tragetory_x, env.tragetory_y, env.tragetory_score)
    # plt.show()




start = time() 
env = Environment(math_function, x_range=(-512, 512), y_range=(-512, 512))
env.start()
duration = time() - start

print('Finished in {:.5} s'.format(duration))

plot_function()

