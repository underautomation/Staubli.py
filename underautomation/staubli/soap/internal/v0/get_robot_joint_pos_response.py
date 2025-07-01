import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJointPosResponse as get_robot_joint_pos_response

class GetRobotJointPosResponse:
	def __init__(self, pos: typing.List[float], _internal = 0):
		if(_internal == 0):
			self._instance = get_robot_joint_pos_response(pos)
		else:
			self._instance = _internal
	@property
	def pos(self) -> typing.List[float]:
		return self._instance.pos
	@pos.setter
	def pos(self, value: typing.List[float]):
		self._instance.pos = value
