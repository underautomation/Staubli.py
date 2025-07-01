import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetRobotDhParametersRequest as get_robot_dh_parameters_request

class GetRobotDhParametersRequest:
	def __init__(self, robot: int, _internal = 0):
		if(_internal == 0):
			self._instance = get_robot_dh_parameters_request(robot)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
