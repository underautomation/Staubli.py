import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.motion_desc import MotionDesc
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveCRequest as move_c_request

class MoveCRequest:
	def __init__(self, robot: int, frameB: Frame, frameC: Frame, mdesc: MotionDesc, _internal = 0):
		if(_internal == 0):
			self._instance = move_c_request(robot, frameB, frameC, mdesc)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
	@property
	def frame_b(self) -> Frame:
		return Frame(self._instance.frameB)
	@frame_b.setter
	def frame_b(self, value: Frame):
		self._instance.frameB = value
	@property
	def frame_c(self) -> Frame:
		return Frame(self._instance.frameC)
	@frame_c.setter
	def frame_c(self, value: Frame):
		self._instance.frameC = value
	@property
	def mdesc(self) -> MotionDesc:
		return MotionDesc(self._instance.mdesc)
	@mdesc.setter
	def mdesc(self, value: MotionDesc):
		self._instance.mdesc = value
