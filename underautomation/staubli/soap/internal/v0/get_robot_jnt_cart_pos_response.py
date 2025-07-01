import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import GetRobotJntCartPosResponse as get_robot_jnt_cart_pos_response

class GetRobotJntCartPosResponse:
	def __init__(self, jntPos: typing.List[float], cartPos: CartesianPosition, _internal = 0):
		if(_internal == 0):
			self._instance = get_robot_jnt_cart_pos_response(jntPos, cartPos)
		else:
			self._instance = _internal
	@property
	def jnt_pos(self) -> typing.List[float]:
		return self._instance.jntPos
	@jnt_pos.setter
	def jnt_pos(self, value: typing.List[float]):
		self._instance.jntPos = value
	@property
	def cart_pos(self) -> CartesianPosition:
		return CartesianPosition(self._instance.cartPos)
	@cart_pos.setter
	def cart_pos(self, value: CartesianPosition):
		self._instance.cartPos = value
