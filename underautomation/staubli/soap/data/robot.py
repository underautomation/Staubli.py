import typing
from underautomation.staubli.soap.data.kinematic import Kinematic
from underautomation.staubli.soap.data.mount_type import MountType
from underautomation.staubli.soap.data.length_axis3 import LengthAxis3
from underautomation.staubli.soap.data.diameter_axis3 import DiameterAxis3
from UnderAutomation.Staubli.Soap.Data import Robot as robot
from UnderAutomation.Staubli.Soap.Data import Kinematic as kinematic
from UnderAutomation.Staubli.Soap.Data import MountType as mount_type
from UnderAutomation.Staubli.Soap.Data import LengthAxis3 as length_axis3
from UnderAutomation.Staubli.Soap.Data import DiameterAxis3 as diameter_axis3

class Robot:
	'''Represents a robot managed by the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the Robot class.'''
		if(_internal == 0):
			self._instance = robot()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def kinematic(self) -> Kinematic:
		'''Kinematic type of the robot.'''
		return Kinematic(int(self._instance.Kinematic))

	@kinematic.setter
	def kinematic(self, value: Kinematic):
		self._instance.Kinematic = kinematic(int(value))

	@property
	def arm(self) -> str:
		'''Arm model identifier.'''
		return self._instance.Arm

	@arm.setter
	def arm(self, value: str):
		self._instance.Arm = value

	@property
	def tuning(self) -> str:
		'''Tuning identifier.'''
		return self._instance.Tuning

	@tuning.setter
	def tuning(self, value: str):
		self._instance.Tuning = value

	@property
	def mount_type(self) -> MountType:
		'''Mounting type of the robot (floor, ceiling, wall).'''
		return MountType(int(self._instance.MountType))

	@mount_type.setter
	def mount_type(self, value: MountType):
		self._instance.MountType = mount_type(int(value))

	@property
	def length_axis3(self) -> LengthAxis3:
		'''Length of the third axis.'''
		return LengthAxis3(int(self._instance.LengthAxis3))

	@length_axis3.setter
	def length_axis3(self, value: LengthAxis3):
		self._instance.LengthAxis3 = length_axis3(int(value))

	@property
	def diameter_axis3(self) -> DiameterAxis3:
		'''Diameter of the third axis.'''
		return DiameterAxis3(int(self._instance.DiameterAxis3))

	@diameter_axis3.setter
	def diameter_axis3(self, value: DiameterAxis3):
		self._instance.DiameterAxis3 = diameter_axis3(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Robot):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
