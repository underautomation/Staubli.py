import typing
from UnderAutomation.Staubli.Soap.Data import JointRange as joint_range

class JointRange:
	'''Minimum and maximum range of each robot joint (radians).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the JointRange class.'''
		if(_internal == 0):
			self._instance = joint_range()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def min(self) -> typing.List[float]:
		'''Minimum values for each joint (radians).'''
		return self._instance.Min

	@min.setter
	def min(self, value: typing.List[float]):
		self._instance.Min = value

	@property
	def max(self) -> typing.List[float]:
		'''Maximum values for each joint (radians).'''
		return self._instance.Max

	@max.setter
	def max(self, value: typing.List[float]):
		self._instance.Max = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointRange):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
