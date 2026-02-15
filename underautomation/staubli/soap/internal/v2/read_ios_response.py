import typing
from underautomation.staubli.soap.data.physical_io_state import PhysicalIoState
from UnderAutomation.Staubli.Soap.Internal.V2 import ReadIosResponse as read_ios_response

class ReadIosResponse:
	'''SOAP response containing the state of physical I/Os.'''
	def __init__(self, state: typing.List[PhysicalIoState], _internal = 0):
		'''Initializes a new instance with the specified I/O states.

		:param state: Array of physical I/O states.
		'''
		if(_internal == 0):
			self._instance = read_ios_response(state)
		else:
			self._instance = _internal

	@property
	def state(self) -> typing.List[PhysicalIoState]:
		'''Array of physical I/O states.'''
		return [PhysicalIoState(x) for x in self._instance.state]

	@state.setter
	def state(self, value: typing.List[PhysicalIoState]):
		self._instance.state = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReadIosResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
