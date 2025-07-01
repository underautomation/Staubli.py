import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJntCartPosRequest as get_robot_jnt_cart_pos_request

class GetRobotJntCartPosRequest:
	def __init__(self, robot: int, tool: CartesianPosition, frame: CartesianPosition, _internal = 0):
		if(_internal == 0):
			self._instance = get_robot_jnt_cart_pos_request(robot, tool, frame)
		else:
			self._instance = _internal
	@property
	def robot(self) -> int:
		return self._instance.robot
	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value
	@property
	def tool(self) -> CartesianPosition:
		return CartesianPosition(self._instance.tool)
	@tool.setter
	def tool(self, value: CartesianPosition):
		self._instance.tool = value
	@property
	def frame(self) -> CartesianPosition:
		return CartesianPosition(self._instance.frame)
	@frame.setter
	def frame(self, value: CartesianPosition):
		self._instance.frame = value
