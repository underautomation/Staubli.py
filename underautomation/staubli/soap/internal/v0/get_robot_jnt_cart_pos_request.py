import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJntCartPosRequest as get_robot_jnt_cart_pos_request

class GetRobotJntCartPosRequest:
	'''SOAP request to retrieve a robot's joint and Cartesian positions.'''
	def __init__(self, robot: int, tool: CartesianPosition, frame: CartesianPosition, _internal = 0):
		'''Initializes a new instance with the specified robot, tool and frame.

		:param robot: Robot identifier.
		:param tool: Tool pose in flange frame.
		:param frame: Reference frame for the Cartesian position.
		'''
		if(_internal == 0):
			self._instance = get_robot_jnt_cart_pos_request(robot, tool, frame)
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
	def tool(self) -> CartesianPosition:
		'''Tool pose in flange frame.'''
		return CartesianPosition(self._instance.tool)

	@tool.setter
	def tool(self, value: CartesianPosition):
		self._instance.tool = value._instance if value else None

	@property
	def frame(self) -> CartesianPosition:
		'''Reference frame for the Cartesian position.'''
		return CartesianPosition(self._instance.frame)

	@frame.setter
	def frame(self, value: CartesianPosition):
		self._instance.frame = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetRobotJntCartPosRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
