import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
from UnderAutomation.Staubli.Soap.Data import CartesianJointPosition as cartesian_joint_position

class CartesianJointPosition:
	'''Represents the joint positions and the Cartesian position of a robot end effector.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_joint_position()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def joints_position(self) -> typing.List[float]:
		'''The joint positions in radians.'''
		return self._instance.JointsPosition

	@joints_position.setter
	def joints_position(self, value: typing.List[float]):
		self._instance.JointsPosition = value

	@property
	def cartesian_position(self) -> CartesianPosition:
		'''The Cartesian position of the robot end effector.'''
		return CartesianPosition(self._instance.CartesianPosition)

	@cartesian_position.setter
	def cartesian_position(self, value: CartesianPosition):
		self._instance.CartesianPosition = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianJointPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
