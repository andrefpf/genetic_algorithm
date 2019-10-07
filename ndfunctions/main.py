import numpy as np
from environment import Environment
from time import time 

def math_function(var):
    return var['x']

def write_file():
    txt = open('results.txt', 'w+')
    
    for value in env.log['scores']:
        txt.write('{:.5f} \n'.format(value))


start = time()

var= ['x']
interval = [(0,2)]
env = Environment(math_function, var, interval, mode='max')
env.start()
write_file()

end = time()

print(f'TIME: {end-start}')
