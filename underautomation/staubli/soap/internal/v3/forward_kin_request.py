import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ForwardKinRequest as forward_kin_request

class ForwardKinRequest:
	def __init__(self, robot: int, joint: typing.List[float], _internal = 0):
		if(_internal == 0):
			self._instance = forward_kin_request(robot, joint)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
	@property
	def joint(self) -> typing.List[float]:
		return self._instance.joint
	@joint.setter
	def joint(self, value: typing.List[float]):
		self._instance.joint = value
