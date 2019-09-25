import random

from chromossome import Chromossome

class Individual:
    def __init__(self, variables, ranges):
        self.chromossomes = self.__create_chromossomes()
        self.variables = []
        self.ranges = []
        self.score = None

    def __create_chromossomes(self):
        chromossomes = []
        for name, rangee in zip(self.variables, self.ranges):
            chromossomes.append(Chromossome(name, rangee))
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
        values = {chromossome.name:chromossome.value for chromossome in self.chromossomes}
        self.score = math_function(values)

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