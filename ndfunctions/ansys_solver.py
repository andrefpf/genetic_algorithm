import os
import time 
from environment import Environment

def write_file(var):
    output_text = open('C:\TESTES_GA\\entrada.txt', 'w+')
    output_text.write('{:14.7E}\n{:14.7E}'.format(var['width'], var['height']))
    output_text.close()

def run_ansys():
    os.system('cd C:\TESTES_GA & ABRE_ANSYS')
    time.sleep(1)

def read_answer():
    input_text = open('C:\TESTES_GA\\resposta.txt', 'r')
    number = abs(float(input_text.read()))
    return number

def math_function(var):
    write_file(var)
    run_ansys()
    answer = read_answer()
    print('WIDTH:{:14.7E}'.format(var['width']))
    print('HEIGHT{:14.7E}'.format(var['height']))
    print('RESULT:{:14.7E}'.format(answer))
    return answer

start = time.time()

var = ['height', 'width']
interval = [(1, 15), (7, 25)]
env = Environment(math_function, var, interval, population_size=10, max_generations=1)
env.start()

end = time.time()
print('TIME:', end-start)