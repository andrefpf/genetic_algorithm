import numpy as np
from environment import Environment
from time import time 

def math_function(var):
    return var['x']

start = time()

var= ['x']
interval = [(0,2)]

env = Environment(math_function, var, interval)
env.start()

print(time() - start)