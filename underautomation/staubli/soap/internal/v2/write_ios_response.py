import typing
from underautomation.staubli.soap.data.physical_io_write_response import PhysicalIoWriteResponse
from UnderAutomation.Staubli.Soap.Internal.V2 import WriteIosResponse as write_ios_response

class WriteIosResponse:
	'''SOAP response containing the results of the I/O write operation.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the WriteIosResponse class.'''
		if(_internal == 0):
			self._instance = write_ios_response()
		else:
			self._instance = _internal

	@property
	def out(self) -> typing.List[PhysicalIoWriteResponse]:
		'''Array of write responses for each I/O.'''
		return [PhysicalIoWriteResponse(x) for x in self._instance.out]

	@out.setter
	def out(self, value: typing.List[PhysicalIoWriteResponse]):
		self._instance.out = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, WriteIosResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
