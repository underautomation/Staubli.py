import typing
from UnderAutomation.Staubli.Soap.Data import PhysicalAioAttribute as physical_aio_attribute

class PhysicalAioAttribute:
	'''Attributes for an analog I/O, including linear conversion coefficients.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PhysicalAioAttribute class.'''
		if(_internal == 0):
			self._instance = physical_aio_attribute()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def coefficient_a(self) -> float:
		'''Linear coefficient A (slope) for analog conversion.'''
		return self._instance.CoefficientA

	@coefficient_a.setter
	def coefficient_a(self, value: float):
		self._instance.CoefficientA = value

	@property
	def coefficient_b(self) -> float:
		'''Linear coefficient B (offset) for analog conversion.'''
		return self._instance.CoefficientB

	@coefficient_b.setter
	def coefficient_b(self, value: float):
		self._instance.CoefficientB = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalAioAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
