import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
from underautomation.staubli.soap.data.joint_range import JointRange
from UnderAutomation.Staubli.Soap.Internal.V3 import ReverseKinRequest as reverse_kin_request

class ReverseKinRequest:
	'''SOAP request to compute reverse (inverse) kinematics for a robot.'''
	def __init__(self, robot: int, jointIn: typing.List[float], target: Frame, config: Config, jointRange: JointRange, _internal = 0):
		'''Initializes a new instance with the specified parameters.

		:param robot: Robot identifier.
		:param jointIn: Initial joint positions in radians.
		:param target: Target Cartesian frame.
		:param config: Robot configuration.
		:param jointRange: Allowed joint range limits.
		'''
		if(_internal == 0):
			self._instance = reverse_kin_request(robot, jointIn, target, config, jointRange)
		else:
			self._instance = _internal

	@property
	def robot(self) -> int:
		'''Robot identifier.'''
		return self._instance.robot

	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value

	@property
	def joint_in(self) -> typing.List[float]:
		'''Initial joint positions in radians.'''
		return self._instance.jointIn

	@joint_in.setter
	def joint_in(self, value: typing.List[float]):
		self._instance.jointIn = value

	@property
	def target(self) -> Frame:
		'''Target Cartesian frame.'''
		return Frame(self._instance.target)

	@target.setter
	def target(self, value: Frame):
		self._instance.target = value._instance if value else None

	@property
	def config(self) -> Config:
		'''Robot configuration.'''
		return Config(self._instance.config)

	@config.setter
	def config(self, value: Config):
		self._instance.config = value._instance if value else None

	@property
	def joint_range(self) -> JointRange:
		'''Allowed joint range limits.'''
		return JointRange(self._instance.jointRange)

	@joint_range.setter
	def joint_range(self, value: JointRange):
		self._instance.jointRange = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReverseKinRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
