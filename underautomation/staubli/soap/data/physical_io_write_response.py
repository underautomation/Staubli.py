import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIoWriteResponse as physical_io_write_response

class PhysicalIoWriteResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_io_write_response()
		else:
			self._instance = _internal
	@property
	def success(self) -> bool:
		return self._instance.Success
	@success.setter
	def success(self, value: bool):
		self._instance.Success = value
	@property
	def found(self) -> bool:
		return self._instance.Found
	@found.setter
	def found(self, value: bool):
		self._instance.Found = value
