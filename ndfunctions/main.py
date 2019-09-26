import numpy as np
from environment import Environment

def math_function(var):
    return var['x']

var= ['x']
interval = [(0,2)]

env = Environment(math_function, var, interval)
env.start()