import random

from individual import Individual

class Environment:
    def __init__(self, math_function, variables, ranges, **kwargs):
        self.math_function = math_function
        self.variables = variables
        self.ranges = ranges

        self.population_size = kwargs.get('population_size', 150)
        self.max_generations = kwargs.get('max_generations', 200)
        self.crossover_rate = kwargs.get('crossover_rate', 1)
        self.mutation_rate = kwargs.get('mutation_rate', 0.01)
        self.mode = kwargs.get('mode', 'min')
        self.elitism = kwargs.get('elitism', 2)

        self.winners_log = []
        self.generation_log = []

        self.generation = 0
        self.population = self.create_population()
        self.winner = None
        self._population_to_evaluate = self.population
    
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
            self.push_winners_log()
            self.push_generation_log()
            self._print_log()
            self.generation += 1

    def _should_continue(self):
        return self.generation < self.max_generations

    def _massive_evaluation(self):
        for individual in self._population_to_evaluate:
            individual.evaluate(self.math_function)
        self._population_to_evaluate = []

    def _set_mode(self):
        if self.mode == 'max':
            self.population = self.population[::-1]

    def _massive_crossover(self):
        population = self.population.copy()
        for position, individual in enumerate(self.population):
            if position < self.elitism: 
                continue
            other = random.choice(population)
            individual.crossover(other, rate=self.crossover_rate)
            self._population_to_evaluate.append(individual)

    def _massive_mutation(self): 
        for position, individual in enumerate(self.population):
            if position < self.elitism: 
                continue
            individual.mutate(rate=self.mutation_rate)
            self._population_to_evaluate.append(individual)
    
    def push_winners_log(self):
        self.winners_log.append(self.winner)

    def push_generation_log(self):
        self.generation_log.append([i.score for i in self.population])
        
    def _print_log(self):
        print('Generation:', self.generation)
        print('Variables:', self.winner.parameters)
        print('Scores:', self.winner.score)
        print()