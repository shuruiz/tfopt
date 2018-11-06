from tensorflow.python.eager import context
from tensorflow.python.framework import ops
from tensorflow.python.ops import control_flow_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import resource_variable_ops
from tensorflow.python.ops import state_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.training import optimizer

class RandomizedHillClimbingOptimizer(optimizer.Optimizer):
	"""
	randomized hill climing optimizer for tensorflow
	hill climbing with random restarts
	"""
	def __init__(self, max_iter = 10000, use_locking = False, name = "RHCopt"):
		
		"""
		Args: 
		"""
		super(RandomizedHillClimbingOptimizer, self).__init__(use_locking, name)

		self._max_iteration = max_iter






	def _create_slots(self, var_list):
		pass 

	def _prepare(self):
		pass 

	def _apply_dense(self,):
		pass 

	def _apply_sparse(self, ):
		pass 



		pass 

class SimulatedAnnealingOptimizer(optimizer.Optimizer):
	def __init__(self, name = 'SIMann'):
		pass 

