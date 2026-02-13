import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
from underautomation.staubli.soap.data.joint_range import JointRange
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ReverseKinRequest as reverse_kin_request

class ReverseKinRequest:
	def __init__(self, robot: int, jointIn: typing.List[float], target: Frame, config: Config, jointRange: JointRange, _internal = 0):
		if(_internal == 0):
			self._instance = reverse_kin_request(robot, jointIn, target, config, jointRange)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
	@property
	def joint_in(self) -> typing.List[float]:
		return self._instance.jointIn
	@joint_in.setter
	def joint_in(self, value: typing.List[float]):
		self._instance.jointIn = value
	@property
	def target(self) -> Frame:
		return Frame(self._instance.target)
	@target.setter
	def target(self, value: Frame):
		self._instance.target = value._instance if value else None
	@property
	def config(self) -> Config:
		return Config(self._instance.config)
	@config.setter
	def config(self, value: Config):
		self._instance.config = value._instance if value else None
	@property
	def joint_range(self) -> JointRange:
		return JointRange(self._instance.jointRange)
	@joint_range.setter
	def joint_range(self, value: JointRange):
		self._instance.jointRange = value._instance if value else None
