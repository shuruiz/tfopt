import numpy as np 
import random 

"""
class to create network
"""


class Network():
	"""create a fully-connected network"""
	def __init__():
		"""
		input layer is not considered as a layer
		"""
		self._nlayer=0
		self._nnodes=[]



	def add_layer(n_nodes,n_layer=1):
		"""
		add layers to the network
		n_nodes: [n_node1, n_nodes_2]
		"""
		self._nlayer +=n_layer
		self._bias  = np.random.randn(self._nlayer) # initialize bias
		
		for ele in n_nodes:
			self._nnodes.append(n_nodes)

	def random_initialize(self):
		for l in range(self._nlayer):
			w = np.random.randn(self._nnodes[l],self._nnodes[l- 1]) 
			self._weights.append(w)

	def getWeights():
		return self._weights

	def output(self):

		return self._output










