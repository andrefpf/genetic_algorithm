import random

class Individual:
    def __init__(self, **kwargs):
        self.cromossome_length = kwargs.get('cromossome_length', 23)
        self.x_range = kwargs.get('x_range', (-2, 2))
        self.alleles = kwargs.get('alleles', (0, 1))

        self.MAX_POSSIBLE = len(self.alleles) ** self.cromossome_length 
        
        self.x = None
        self.score = None
        self.chromossomes = self.new_cromossome()

    def new_cromossome(self):
        return [random.choice(self.alleles) for i in range(self.cromossome_length)]

    def have_some_sex(self, other):
        left, right = self.genes_to_exchange()
        self.chromossomes[left:right] = other.chromossomes[left:right]
    
    def mutate(self):
        gene_position = random.randint(0, self.cromossome_length-1)
        self.chromossomes[gene_position] = 0 if self.chromossomes[gene_position] else 1
    
    def genes_to_exchange(self):
        left = random.randint(0, self.cromossome_length-1)
        right = random.randint(left, self.cromossome_length)
        return (left, right)
    
    def evaluate(self, math_function):
        chromossomes = ''.join([str(i) for i in self.chromossomes])
        interval = self.x_range[1] - self.x_range[0]
        mapping = int(chromossomes, 2) * interval / self.MAX_POSSIBLE

        self.x = self.x_range[0] + mapping
        self.score = math_function(self.x)