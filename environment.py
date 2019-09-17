import random
import math
from individual import Individual

class Environment:
    def __init__(self, math_function, **kwargs):
        self.size = kwargs.get('size', 100)
        self.sex_rate = kwargs.get('sex_rate', 1)
        self.mutation_rate = kwargs.get('mutation_rate', 0.01)
        self.max_generations = kwargs.get('max_generations', 200)

        self.math_function = math_function
        self.maximize = kwargs.get('maximize', False)
        self.x_range = kwargs.get('x_range', (-1,1))
        self.y_range = kwargs.get('y_range', (-1,1))

        self.tragetory_x = []
        self.tragetory_y = []
        self.tragetory_score = []

        self.generation = 0
        self.population = self.create_population()
        self.winner = None
    
    def create_population(self):
        return [Individual(x_range=self.x_range, y_range=self.y_range) for i in range(self.size)]

    def start(self):
        while self.generation < self.max_generations:
            self._fight()
            self.population = self.sort_score(self.population)
            self._massive_sex()
            self._mutate()
            self.winner = self.population[0]
            self._show_info()
            self._set_tragetory()
            self.generation += 1

    def _fight(self):
        for individual in self.population:
            individual.evaluate(self.math_function)

    def sort_score(self, array):
        if len(array) >= 2:
            left_array = []
            right_array  = []
            center_array = []
            pivot = array[-1]

            if self.maximize:
                for individual in array:
                    if individual.score > pivot.score:
                        left_array.append(individual)
                    elif individual.score < pivot.score:
                        right_array.append(individual)    
                    elif individual.score == pivot.score:
                        center_array.append(individual)
            else:
                for individual in array:
                    if individual.score < pivot.score:
                        left_array.append(individual)
                    elif individual.score > pivot.score:
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
            if i > 1 and random.random() < self.sex_rate:
                other = random.choice(self.population)
                self.population[i].have_some_sex(other)

    def _mutate(self):
        for i in range(self.size):
            if i > 1 and random.random() < self.mutation_rate:
                pass
                self.population[i].mutate()

    def _set_tragetory(self):
        self.tragetory_x.append(self.winner.x)
        self.tragetory_y.append(self.winner.y)
        self.tragetory_score.append(self.winner.score)

    def _show_info(self):
        print('='*20)
        print(f'Generation: {self.generation}')
        print(f'Result: {self.winner.score}')
        print(f'X: {self.winner.x}')
        print(f'Y: {self.winner.y}')
        print(f'Chromossome_x: {str(self.winner.chromossome_x)}')
        print(f'Chromossome_y: {str(self.winner.chromossome_y)}')
        print('='*20)
