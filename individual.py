import random

class Individual:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
        self.cromossome_length = 23
        self.alleles = (0, 1)
        self.MAX_POSSIBLE = len(self.alleles) ** self.cromossome_length 
        
        self.x = None
        self.y = None
        self.score = None
        self.chromossome_x = self.new_cromossome()
        self.chromossome_y = self.new_cromossome()

    def new_cromossome(self):
        return [random.choice(self.alleles) for i in range(self.cromossome_length)]

    def have_some_sex(self, other):
        left, right = self._genes_to_exchange()
        self.chromossome_x[left:right] = other.chromossome_x[left:right]

        left, right = self._genes_to_exchange()
        self.chromossome_y[left:right] = other.chromossome_y[left:right]
    
    def mutate(self):
        gene_position = random.randint(0, self.cromossome_length-1)
        self.chromossome_x[gene_position] = 0 if self.chromossome_x[gene_position] else 1

        gene_position = random.randint(0, self.cromossome_length-1)
        self.chromossome_y[gene_position] = 0 if self.chromossome_y[gene_position] else 1
    
    def _genes_to_exchange(self):
        left = random.randint(0, self.cromossome_length-1)
        right = random.randint(left, self.cromossome_length)
        return (left, right)
    
    def evaluate(self, math_function):
        chromossome_x = ''.join([str(i) for i in self.chromossome_x])
        interval_x = self.x_range[1] - self.x_range[0]
        mapping_x = int(chromossome_x, 2) * interval_x / self.MAX_POSSIBLE

        chromossome_y = ''.join([str(i) for i in self.chromossome_y])
        interval_y = self.y_range[1] - self.y_range[0]
        mapping_y = int(chromossome_y, 2) * interval_y / self.MAX_POSSIBLE

        self.x = self.x_range[0] + mapping_x
        self.y = self.y_range[0] + mapping_y
        self.score = math_function(self.x, self.y)