from time import time 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np 
from environment import Environment

def math_function(x, y=0):
    # return 100 * np.sqrt(np.abs(y - (0.01 * x**2))) + 0.01*np.abs(x + 10)
    # return -(y + 47) * np.sin(np.sqrt(np.abs(y + x/2 + 47))) - x*np.sin(np.sqrt(np.abs(x-(y+47))))
    # return x**2 + y**2
    return 418.9829*2 - x*np.sin(np.sqrt(np.abs(x))) - y*np.sin(np.sqrt(np.abs(y)))

def get_nice_scale():
    x_r = x_range[1] - x_range[0]
    y_r = y_range[1] - y_range[0]
    return min(x_r, y_r) * 0.03

def plot_function():
    scale = get_nice_scale()
    x = np.arange(x_range[0], x_range[1], scale)
    y = np.arange(y_range[0], y_range[1], scale)
    x, y = np.meshgrid(x, y)
    z = math_function(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z, cmap=cm.coolwarm, alpha=0.5)
    ax.scatter(env.tragetory_x, env.tragetory_y, env.tragetory_score, c='r')

    ax.text2D(0.05, 1.10, f'Aproximated X axis = {env.winner.x}', transform=ax.transAxes)
    ax.text2D(0.05, 1.05, f'Aproximated Y axis = {env.winner.y}', transform=ax.transAxes)
    ax.text2D(0.05, 1.00, f'Aproximated Result = {env.winner.score}', transform=ax.transAxes)
    plt.show()

x_range = (-500, 500)
y_range = (-500, 500)
start = time() 
env = Environment(math_function, 
                  x_range=x_range, 
                  y_range=y_range,
                  maximize=False,
                  max_generations=300,
                  size=200,)
env.start()
duration = time() - start

print('Finished in {:.5} s'.format(duration))

plot_function()

