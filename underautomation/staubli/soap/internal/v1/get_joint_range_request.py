import typing
from UnderAutomation.Staubli.Soap.Internal.V1 import GetJointRangeRequest as get_joint_range_request

class GetJointRangeRequest:
	'''SOAP request to retrieve a robot's joint range limits.'''
	def __init__(self, robot: int, _internal = 0):
		'''Initializes a new instance with the specified robot identifier.

		:param robot: Robot identifier.
		'''
		if(_internal == 0):
			self._instance = get_joint_range_request(robot)
		else:
			self._instance = _internal

	@property
	def robot(self) -> int:
		'''Robot identifier.'''
		return self._instance.robot

	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetJointRangeRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
