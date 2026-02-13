import typing
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import CartesianJointPosition as cartesian_joint_position

class CartesianJointPosition:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_joint_position()
		else:
			self._instance = _internal
	@property
	def joints_position(self) -> typing.List[float]:
		return self._instance.JointsPosition
	@joints_position.setter
	def joints_position(self, value: typing.List[float]):
		self._instance.JointsPosition = value
	@property
	def cartesian_position(self) -> CartesianPosition:
		return CartesianPosition(self._instance.CartesianPosition)
	@cartesian_position.setter
	def cartesian_position(self, value: CartesianPosition):
		self._instance.CartesianPosition = value._instance if value else None
