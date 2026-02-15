import typing
from UnderAutomation.Staubli.Soap.Data import DhParameters as dh_parameters

class DhParameters:
	'''Denavit-Hartenberg parameters for a single robot joint.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the DhParameters class.'''
		if(_internal == 0):
			self._instance = dh_parameters()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def theta(self) -> float:
		'''Joint angle theta (radians).'''
		return self._instance.Theta

	@theta.setter
	def theta(self, value: float):
		self._instance.Theta = value

	@property
	def d(self) -> float:
		'''Link offset d (m).'''
		return self._instance.D

	@d.setter
	def d(self, value: float):
		self._instance.D = value

	@property
	def a(self) -> float:
		'''Link length a (m).'''
		return self._instance.A

	@a.setter
	def a(self, value: float):
		self._instance.A = value

	@property
	def alpha(self) -> float:
		'''Link twist alpha (radians).'''
		return self._instance.Alpha

	@alpha.setter
	def alpha(self, value: float):
		self._instance.Alpha = value

	@property
	def beta(self) -> float:
		'''Joint twist beta (radians).'''
		return self._instance.Beta

	@beta.setter
	def beta(self, value: float):
		self._instance.Beta = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DhParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
