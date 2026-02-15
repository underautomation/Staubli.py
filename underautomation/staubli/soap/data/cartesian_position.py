import typing
from UnderAutomation.Staubli.Soap.Data import CartesianPosition as cartesian_position

class CartesianPosition:
	'''Represents a Cartesian position with X, Y, Z translation and Rx, Ry, Rz rotation components.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CartesianPosition class.'''
		if(_internal == 0):
			self._instance = cartesian_position()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def x(self) -> float:
		'''X translation component (m).'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y translation component (m).'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z translation component (m).'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	@property
	def rx(self) -> float:
		'''Rotation around the X axis (radians).'''
		return self._instance.Rx

	@rx.setter
	def rx(self, value: float):
		self._instance.Rx = value

	@property
	def ry(self) -> float:
		'''Rotation around the Y axis (radians).'''
		return self._instance.Ry

	@ry.setter
	def ry(self, value: float):
		self._instance.Ry = value

	@property
	def rz(self) -> float:
		'''Rotation around the Z axis (radians).'''
		return self._instance.Rz

	@rz.setter
	def rz(self, value: float):
		self._instance.Rz = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
