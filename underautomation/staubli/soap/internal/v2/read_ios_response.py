import typing
from underautomation.staubli.soap.data.physical_io_state import PhysicalIoState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import ReadIosResponse as read_ios_response

class ReadIosResponse:
	def __init__(self, state: typing.List[PhysicalIoState], _internal = 0):
		if(_internal == 0):
			self._instance = read_ios_response(state)
		else:
			self._instance = _internal
	@property
	def state(self) -> typing.List[PhysicalIoState]:
		return [PhysicalIoState(x) for x in self._instance.state]
	@state.setter
	def state(self, value: typing.List[PhysicalIoState]):
		self._instance.state = value._instance if value else None
