import typing
from UnderAutomation.Staubli.Soap.Internal.V3 import ForwardKinRequest as forward_kin_request

class ForwardKinRequest:
	'''SOAP request to compute forward kinematics for a robot.'''
	def __init__(self, robot: int, joint: typing.List[float], _internal = 0):
		'''Initializes a new instance with the specified robot and joint positions.

		:param robot: Robot identifier.
		:param joint: Joint positions in radians.
		'''
		if(_internal == 0):
			self._instance = forward_kin_request(robot, joint)
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
	def joint(self) -> typing.List[float]:
		'''Joint positions in radians.'''
		return self._instance.joint

	@joint.setter
	def joint(self, value: typing.List[float]):
		self._instance.joint = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ForwardKinRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
