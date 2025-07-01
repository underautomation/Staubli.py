import typing
from underautomation.staubli.soap.data.robot import Robot
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotsResponse as get_robots_response

class GetRobotsResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_robots_response()
		else:
			self._instance = _internal
	@property
	def out(self) -> typing.List[Robot]:
		return [Robot(x) for x in self._instance.out]
	@out.setter
	def out(self, value: typing.List[Robot]):
		self._instance.out = value
