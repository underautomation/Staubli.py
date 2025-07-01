import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V1 import GetJointRangeRequest as get_joint_range_request

class GetJointRangeRequest:
	def __init__(self, robot: int, _internal = 0):
		if(_internal == 0):
			self._instance = get_joint_range_request(robot)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
