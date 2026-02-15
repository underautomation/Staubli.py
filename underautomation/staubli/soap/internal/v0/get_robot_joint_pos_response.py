import typing
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJointPosResponse as get_robot_joint_pos_response

class GetRobotJointPosResponse:
	'''SOAP response containing a robot's joint positions.'''
	def __init__(self, pos: typing.List[float], _internal = 0):
		'''Initializes a new instance with the specified joint positions.

		:param pos: Joint positions in radians.
		'''
		if(_internal == 0):
			self._instance = get_robot_joint_pos_response(pos)
		else:
			self._instance = _internal

	@property
	def pos(self) -> typing.List[float]:
		'''Joint positions in radians.'''
		return self._instance.pos

	@pos.setter
	def pos(self, value: typing.List[float]):
		self._instance.pos = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetRobotJointPosResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
