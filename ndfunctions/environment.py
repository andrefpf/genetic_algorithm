import random

from individual import Individual

class Environment:
    def __init__(self, math_function, variables, ranges, **kwargs):
        self.math_function = math_function
        self.variables = variables
        self.ranges = ranges

        self.population_size = kwargs.get('population_size', 150)
        self.crossover_rate = kwargs.get('crossover_rate', 1)
        self.mutation_rate = kwargs.get('mutation_rate', 0.01)
        self.max_generations = kwargs.get('max_generations', 200)
        self.mode = kwargs.get('mode', 'Min')
        self.elitism = kwargs.get('elitism', 2)

        self.tragetory_score = []
        self.generation = 0
        self.population = self.create_population()
        self.winner = None
    
    def create_population(self):
        return [Individual(self.variables, self.ranges) for i in range(self.population_size)]

    def start(self):
        while self._should_continue():
            self._massive_evaluation()
            self.population.sort()
            self._set_mode()
            self.winner = self.population[0]
            self._massive_crossover()
            self._massive_mutation()
            self._show_info()
            self.generation += 1

    def _should_continue(self):
        return self.generation < self.max_generations

    def _massive_evaluation(self):
        for individual in self.population:
            individual.evaluate(self.math_function)

    def _set_mode(self):
        if self.mode == 'Max':
            self.population = self.population[::-1]

    def _massive_crossover(self):
        population = self.population.copy()
        for position, individual in enumerate(self.population):
            if position < self.elitism: continue
            other = random.choice(population)
            individual.crossover(other, rate=self.crossover_rate)

    def _massive_mutation(self): 
        for position, individual in enumerate(self.population):
            if position < self.elitism: continue
            individual.mutate(rate=self.crossover_rate)

    def _show_info(self):
        print('Generation {}'.format(self.generation))
        print('Variables {}'.format(self.winner.show_chromossomes()))
        print('Score {}'.format(self.winner.score))
        print()
        