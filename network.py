import numpy as np 
import random 

"""
class to create network
"""
# from genetic_algorithm import GeneticAlgorithmTrainner



class Network():
	"""create a fully-connected network"""
	def __init__(self, nn_structure):
		"""
		input layer is not considered as a layer
		"""
		# self.structure=nn_structure
		self._nlayer=len(nn_structure)-1
		# print("layers",self._nlayer)
		self._nnodes=nn_structure[1:]
		self._num_input = nn_structure[0][0]
		self._input_dim = nn_structure[0][1]

		# print("_num_input:", self._num_input)
		self._weights={} #{layer: Weights}
		self._bias={}
		self.random_initialize()

	def add_layer(self,n_nodes):
		"""
		add layers to the network
		n_nodes: [n_node1, n_nodes_2]
		"""
		n_layer = len(n_nodes)

		self._nlayer +=n_layer
		# self._bias  = np.random.randn(1, self._nlayer) # initialize bias
		for ele in n_nodes:
			self._nnodes.append(n_nodes)
		self.random_initialize()


	def random_initialize(self):
		for l in range(self._nlayer):
			
			Weights = []

			if l ==0: # first layer
				for n in range(self._nnodes[l]):
					Weights = np.random.randn(self._input_dim, self._nnodes[l])
					self._bias[l]  = np.random.randn(self._num_input,self._nnodes[l])
					# Weights.append(w)
				# Weights = np.array(Weights)
				self._weights[l] = Weights

			else:
				for n in range(self._nnodes[l]):
					Weights= np.random.randn(self._nnodes[l-1], self._nnodes[l])
					self._bias[l]  = np.random.randn(self._num_input,self._nnodes[l])
					# Weights.append(w[0])
				# Weights = np.array(Weights)
				self._weights[l] = Weights

		# print("random initialize weights")

	# def train(self, data, problem, episodes = 100000, algo='genetic'):
	# 	"""

	# 	"""

	# 	if algo == genetic:
	# 		for epi in range(episodes):
	# 			self._weights, self._bias, fitness = GeneticAlgorithmTrainner(self._weights, self.bias, problem)

	# 	elif algo =='RHC':
	# 		pass 
	# 	elif algo =='SIMann':
	# 		pass 


	def getWeights(self):
		return self._weights

	def getBias(self):
		return self._bias

	def setWeights(self,W):
		for l in range(self._nlayer):
			self._weights[l] = W[l]

	def setBias(self, B):
		for l in range(self._nlayer):
			self._bias[l] = B[l]












