import typing
from underautomation.staubli.soap.data.motion_desc import MotionDesc
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveJJRequest as move_jj_request

class MoveJJRequest:
	def __init__(self, robot: int, joint: typing.List[float], mdesc: MotionDesc, _internal = 0):
		if(_internal == 0):
			self._instance = move_jj_request(robot, joint, mdesc)
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
	@property
	def mdesc(self) -> MotionDesc:
		return MotionDesc(self._instance.mdesc)
	@mdesc.setter
	def mdesc(self, value: MotionDesc):
		self._instance.mdesc = value._instance if value else None
