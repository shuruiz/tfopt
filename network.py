import numpy as np 
import random 

"""
class to create network
"""

class Network():
	"""create a fully-connected network"""
	def __init__(n_layers = 3, layer_size = [40,20, 10] ):
		"""
		input layer is not considered as a layer
		"""
		self._n_layers = n_layers 
		self._layer_size = layer_size

		self._weights=[]
		
	def random_initialize(self):
		for l in range(n_layers):
			w = np.random.randn(layer_size[l],layer_size[l- 1 ]) * 0.01
			self._weights.append(w)





