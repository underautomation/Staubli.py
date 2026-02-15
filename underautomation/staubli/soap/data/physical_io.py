import typing
from UnderAutomation.Staubli.Soap.Data import PhysicalIo as physical_io

class PhysicalIo:
	'''Represents a physical I/O on the robot.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_io()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''Name of the physical I/O.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def description(self) -> str:
		'''Description of the physical I/O.'''
		return self._instance.Description

	@description.setter
	def description(self, value: str):
		self._instance.Description = value

	@property
	def type_str(self) -> str:
		'''Type of the physical I/O (e.g., din, dout, ain, serial, ...).'''
		return self._instance.TypeStr

	@type_str.setter
	def type_str(self, value: str):
		self._instance.TypeStr = value

	@property
	def lockable(self) -> bool:
		'''Indicates whether the physical I/O is lockable.'''
		return self._instance.Lockable

	@lockable.setter
	def lockable(self, value: bool):
		self._instance.Lockable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalIo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
