import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJntCartPosResponse as get_robot_jnt_cart_pos_response

class GetRobotJntCartPosResponse:
	'''SOAP response containing the robot's joint and Cartesian positions.'''
	def __init__(self, jntPos: typing.List[float], cartPos: CartesianPosition, _internal = 0):
		'''Initializes a new instance with the specified joint and Cartesian positions.

		:param jntPos: Joint positions in radians.
		:param cartPos: Cartesian position of the tool.
		'''
		if(_internal == 0):
			self._instance = get_robot_jnt_cart_pos_response(jntPos, cartPos)
		else:
			self._instance = _internal

	@property
	def jnt_pos(self) -> typing.List[float]:
		'''Joint positions in radians.'''
		return self._instance.jntPos

	@jnt_pos.setter
	def jnt_pos(self, value: typing.List[float]):
		self._instance.jntPos = value

	@property
	def cart_pos(self) -> CartesianPosition:
		'''Cartesian position of the tool.'''
		return CartesianPosition(self._instance.cartPos)

	@cart_pos.setter
	def cart_pos(self, value: CartesianPosition):
		self._instance.cartPos = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetRobotJntCartPosResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
