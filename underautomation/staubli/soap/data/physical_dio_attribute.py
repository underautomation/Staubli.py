import typing
from UnderAutomation.Staubli.Soap.Data import PhysicalDioAttribute as physical_dio_attribute

class PhysicalDioAttribute:
	'''Attributes for a digital I/O.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PhysicalDioAttribute class.'''
		if(_internal == 0):
			self._instance = physical_dio_attribute()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def inverted(self) -> bool:
		'''Indicates whether the digital I/O logic is inverted.'''
		return self._instance.Inverted

	@inverted.setter
	def inverted(self, value: bool):
		self._instance.Inverted = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalDioAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
