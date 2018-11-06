
import numpy as np 
import random 
from network import Network 

def _create_population(size=100):
	"""
	size: population size, number of chromesomes 

	return population, which is a list of random created network graphs
	"""
	population = []
	for _ in range(size):
		nn = Network()
		nn.random_initialize() #  shape 
		population .append(nn)
	return population



def GeneticAlgorithmTrainner():
	pop = _create_population()


def fitness(nn, X):
	## 1/ cross_entropy 
	W = nn.getWeights()
	b = nn.getBias()
	n_layer = len(W)














class GeneticAlgorithmOptimizer():

	def __init__(self, num_input, mutation_rate = 0.2, random_select = 0.1, retain = 0.4, name = 'GA'):
		self._mutation_rate = mutation_rate
		self._random_select = random_select
		self._retain = retain 
		# self._list_of_target = targets




	def encode(self,nn):  # weights 
		# algorithm ref: 
		# Montana, D. J., & Davis, L. (1989, August). \
		# Training Feedforward Neural Networks Using Genetic Algorithms. \
		# In IJCAI (Vol. 89, pp. 762-767).
		_weights = nn.getWeights()
		gene  = [x for x in _weights]
		return gene 

	def breed(self, mother, father):
		children=[]

		for i in range(2):
			child = {}

	

