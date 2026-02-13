import typing
from underautomation.staubli.soap.data.physical_io_write_response import PhysicalIoWriteResponse
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import WriteIosResponse as write_ios_response

class WriteIosResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = write_ios_response()
		else:
			self._instance = _internal
	@property
	def out(self) -> typing.List[PhysicalIoWriteResponse]:
		return [PhysicalIoWriteResponse(x) for x in self._instance.out]
	@out.setter
	def out(self, value: typing.List[PhysicalIoWriteResponse]):
		self._instance.out = value._instance if value else None
