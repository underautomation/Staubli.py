import typing
from UnderAutomation.Staubli.Soap.Data import ValApplication as val_application

class ValApplication:
	'''Represents a VAL3 application on the controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = val_application()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''Name of the application.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def loaded(self) -> bool:
		'''Indicates whether the application is loaded in memory.'''
		return self._instance.Loaded

	@loaded.setter
	def loaded(self, value: bool):
		self._instance.Loaded = value

	@property
	def is_crypted(self) -> bool:
		'''Indicates whether the application is encrypted.'''
		return self._instance.IsCrypted

	@is_crypted.setter
	def is_crypted(self, value: bool):
		self._instance.IsCrypted = value

	@property
	def is_running(self) -> bool:
		'''Indicates whether the application is currently running.'''
		return self._instance.IsRunning

	@is_running.setter
	def is_running(self, value: bool):
		self._instance.IsRunning = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ValApplication):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
