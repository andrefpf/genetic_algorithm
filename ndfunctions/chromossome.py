import numpy as np

class Chromossome:
    def __init__(self, name, interval):
        self.name = name
        self.interval = interval
        self.length = 10
        self.alleles = (0, 1)
        self.genes = self.create_genes()

    @property
    def value(self):
        base = len(self.alleles)
        gene_string = ''.join([str(i) for i in self.genes])
        decimal = int(gene_string, base)
        return self._map_to_interval(decimal)

    def create_genes(self):
        array = np.random.choice(self.alleles, size=self.length)
        return array.tolist()
    
    def mutate(self):
        position = np.random.randint(self.length)
        self.genes[position] = 0 if self.genes[position] else 1
    
    def exchange(self, other): 
        start, end = self._genes_to_exchange()
        self.genes[start:end] = other.genes[start:end]

    def _map_to_interval(self, decimal):
        base = len(self.alleles)
        max_possible = base**self.length -1
        difference = self.interval[1] - self.interval[0]
        return self.interval[0] + (decimal * difference / max_possible)

    def _genes_to_exchange(self):
        start = np.random.randint(0, self.length-1)
        end = np.random.randint(start, self.length)
        return (start,end)
    