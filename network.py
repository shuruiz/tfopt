import numpy as np 
import random 

"""
class to create network
"""
# from genetic_algorithm import GeneticAlgorithmTrainner



class Network():
	"""create a fully-connected network"""
	def __init__(num_input):
		"""
		input layer is not considered as a layer
		"""
		self._nlayer=0
		self._nnodes=[]
		self._num_input = num_input
		self._weights={} #{layer: Weights}
		self._bias={}

	def add_layer(n_nodes):
		"""
		add layers to the network
		n_nodes: [n_node1, n_nodes_2]
		"""
		n_layer = len(n_nodes)

		self._nlayer +=n_layer
		# self._bias  = np.random.randn(1, self._nlayer) # initialize bias
		for ele in n_nodes:
			self._nnodes.append(n_nodes)
		random_initialize()


	def random_initialize(self):
		for l in range(self._nlayer):
			self._bias[l]  = np.random.randn()
			Weights = []
			if l ==0: # first layer
				for n in range(self._nnodes[l]):
					w = np.random.randn(1,self._num_input)
					Weights.append(w[0])
				Weights = np.array(Weights)
				self._weights[l] = Weights

			else:
				for n in range(self._nnodes[l]):
					w = np.random.randn(1, self._nnodes[l-1])
					Weights.append(w[0])
				Weights = np.array(Weights)
				self._weights[l] = Weights

	def train(data, problem, episodes = 100000, algo='genetic'):
		"""

		"""

		if algo == genetic:
			for epi in range(episodes):
				self._weights, self._bias, fitness = GeneticAlgorithmTrainner(self._weights, self.bias, problem)

		elif algo =='RHC':
			pass 
		elif algo =='SIMann':
			pass 


	def getWeights():
		return self._weights
	def getBias():
	return self._bias

	def setWeights(W):
		for l in range(self._nlayer):
			self._weights[l] = W[l]

	def setBias(B):
		for l in range(self._nlayer):
			self._bias[l] = B[l]












