# from tensorflow.python.eager import context
# from tensorflow.python.framework import ops
# from tensorflow.python.ops import control_flow_ops
# from tensorflow.python.ops import math_ops
# from tensorflow.python.ops import resource_variable_ops
# from tensorflow.python.ops import state_ops
# from tensorflow.python.ops import variable_scope
# from tensorflow.python.training import optimizer

import numpy as np 
import random 
from network import Network 

class GeneticAlgorithmOptimizer():

	def __init__(self, target, mutation_rate = 0.2, random_select = 0.1, retain = 0.4, name = 'GA'):
		self._mutation_rate = mutation_rate
		self._random_select = random_select
		self._retain = retain 
		self._list_of_target = targets


	def _create_population(self, size):
		"""
		size: population size, number of chromesomes 

		return population, which is a list of random created network graphs
		"""
		population = []
		for _ in range(size):
			nn = Network()
			nn.random_initialize()

			population .append(nn)
		return population


	@staticmethod
	def fitness(nn, problem='k-peak'):
		"""
		return the sore of current network
		"""
		if problem == 'k-peak':
			fitness = 

		elif problem =='k-color':
			fitness = 

		else:
			print("you problem should be 'k-peak' or 'k-color' ")
			return None 
		return fitness

	def encode(self,nn): # weights + bias
		_weights = nn.getWeights()
		gene  = [x for x in _weights]
		return gene 


	def breed(self, mother, father ):
		children=[]

		for i in range(2):
			child = {}

			# get weights for the kids
			for weight in self.

