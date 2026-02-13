import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.motion_desc import MotionDesc
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveJCRequest as move_jc_request

class MoveJCRequest:
	def __init__(self, robot: int, frame: Frame, mdesc: MotionDesc, _internal = 0):
		if(_internal == 0):
			self._instance = move_jc_request(robot, frame, mdesc)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
	@property
	def frame(self) -> Frame:
		return Frame(self._instance.frame)
	@frame.setter
	def frame(self, value: Frame):
		self._instance.frame = value._instance if value else None
	@property
	def mdesc(self) -> MotionDesc:
		return MotionDesc(self._instance.mdesc)
	@mdesc.setter
	def mdesc(self, value: MotionDesc):
		self._instance.mdesc = value._instance if value else None
