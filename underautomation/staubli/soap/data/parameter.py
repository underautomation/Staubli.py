import typing
from UnderAutomation.Staubli.Soap.Data import Parameter as parameter

class Parameter:
	'''Key-value parameter from the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the Parameter class.'''
		if(_internal == 0):
			self._instance = parameter()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def key(self) -> str:
		'''Parameter key identifier.'''
		return self._instance.Key

	@key.setter
	def key(self, value: str):
		self._instance.Key = value

	@property
	def name(self) -> str:
		'''Display name of the parameter.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def value(self) -> str:
		'''Value of the parameter.'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Parameter):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
