import random
import math
from individual import Individual

class Environment:
    def __init__(self):
        self.size = 100
        self.max_generations = 200
        self.mutation_rate = 0.01
        self.sex_rate = 1

        self.generation = 0
        self.population = self.create_population()
        self.winner = None
    
    def create_population(self):
        return [Individual() for i in range(self.size)]

    def loop(self):
        while self.generation < self.max_generations:
            self._fight()
            self.population = self.sort_score(self.population)
            self._massive_sex()
            self._mutate()
            self.winner = self.population[0]
            self._show_info()
            self.generation += 1 
        print('x =', self.winner.x)
        print('y =', self.winner.score)

    def _fight(self):
        for individual in self.population:
            individual.evaluate(self.math_function)

    def sort_score(self, array):
        if len(array) >= 2:
            left_array = []
            right_array  = []
            center_array = []
            pivot = array[-1]
            for individual in array:
                if individual.score > pivot.score:
                    left_array.append(individual)
                elif individual.score < pivot.score:
                    right_array.append(individual)    
                elif individual.score == pivot.score:
                    center_array.append(individual)

            left_array = self.sort_score(left_array)
            right_array  = self.sort_score(right_array)
            return left_array + center_array + right_array
        else:
            return array

    def _massive_sex(self):
        for i in range(self.size):
            if i > 5 and random.random() < self.sex_rate:
                other = random.choice(self.population)
                self.population[i].have_some_sex(other)

    def _mutate(self):
        for i in range(self.size):
            if i > 5 and random.random() < self.mutation_rate:
                pass
                self.population[i].mutate()

    def _show_info(self):
        print('='*20)
        print(f'Generation: {self.generation}')
        print(f'Result: {self.winner.score}')
        print(f'X: {self.winner.x}')
        print(f'Chromossome: {str(self.winner.chromossomes)}')
        print('='*20)

    def math_function(self, x):
        return math.sin(x*5) * (x**3)/19 -x 