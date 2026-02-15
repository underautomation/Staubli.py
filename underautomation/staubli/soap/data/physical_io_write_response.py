import typing
from UnderAutomation.Staubli.Soap.Data import PhysicalIoWriteResponse as physical_io_write_response

class PhysicalIoWriteResponse:
	'''Result of a physical I/O write operation.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PhysicalIoWriteResponse class.'''
		if(_internal == 0):
			self._instance = physical_io_write_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def success(self) -> bool:
		'''Indicates whether the write operation succeeded.'''
		return self._instance.Success

	@success.setter
	def success(self, value: bool):
		self._instance.Success = value

	@property
	def found(self) -> bool:
		'''Indicates whether the specified I/O was found.'''
		return self._instance.Found

	@found.setter
	def found(self, value: bool):
		self._instance.Found = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalIoWriteResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
