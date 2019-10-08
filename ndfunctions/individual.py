import random

from chromossome import Chromossome

class Individual:
    def __init__(self, variables, intervals):
        self.score = None
        self.variables = variables
        self.intervals = intervals
        self.chromossomes = self.__create_chromossomes()

    @property
    def parameters(self):
        return {chromossome.name:chromossome.value for chromossome in self.chromossomes}

    def __create_chromossomes(self):
        chromossomes = []
        for name, interval in zip(self.variables, self.intervals):
            chromossomes.append(Chromossome(name, interval))
        return chromossomes

    def crossover(self, other, rate=1):
        if random.random() > rate: return 
        for me, them in zip(self.chromossomes, other.chromossomes):
            me.exchange(them)

    def mutate(self, rate=1):
        for chromossome in self.chromossomes:
            if random.random() > rate: continue
            chromossome.mutate()
    
    def evaluate(self, math_function):
        self.score = math_function(self.parameters)

    def show_chromossomes(self):
        chromossomes = dict()
        for chromossome in self.chromossomes:
            chromossomes[chromossome.name] = chromossome.value
        return chromossomes

    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score
    
    def __le__(self, other):
        return self.score <= other.score
    
    def __ge__(self, other):
        return self.score >= other.score
    
    def __eq__(self, other):
        return self.score == other.score