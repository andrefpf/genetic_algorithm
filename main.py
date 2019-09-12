from environment import Environment
from time import time 

start = time()
env = Environment()
env.loop()
duration = time() - start
print('Finished in {:.5} ms'.format(duration))