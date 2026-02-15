import typing
from underautomation.staubli.soap.data.robot import Robot
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotsResponse as get_robots_response

class GetRobotsResponse:
	'''SOAP response containing the list of robots.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetRobotsResponse class.'''
		if(_internal == 0):
			self._instance = get_robots_response()
		else:
			self._instance = _internal

	@property
	def out(self) -> typing.List[Robot]:
		'''Array of robots managed by the controller.'''
		return [Robot(x) for x in self._instance.out]

	@out.setter
	def out(self, value: typing.List[Robot]):
		self._instance.out = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetRobotsResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
