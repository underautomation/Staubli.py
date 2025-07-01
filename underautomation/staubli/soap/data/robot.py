import typing
from underautomation.staubli.soap.data.kinematic import Kinematic
from underautomation.staubli.soap.data.mount_type import MountType
from underautomation.staubli.soap.data.length_axis3 import LengthAxis3
from underautomation.staubli.soap.data.diameter_axis3 import DiameterAxis3
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Robot as robot

class Robot:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = robot()
		else:
			self._instance = _internal
	@property
	def kinematic(self) -> Kinematic:
		return Kinematic(self._instance.Kinematic)
	@kinematic.setter
	def kinematic(self, value: Kinematic):
		self._instance.Kinematic = value
	@property
	def arm(self) -> str:
		return self._instance.Arm
	@arm.setter
	def arm(self, value: str):
		self._instance.Arm = value
	@property
	def tuning(self) -> str:
		return self._instance.Tuning
	@tuning.setter
	def tuning(self, value: str):
		self._instance.Tuning = value
	@property
	def mount_type(self) -> MountType:
		return MountType(self._instance.MountType)
	@mount_type.setter
	def mount_type(self, value: MountType):
		self._instance.MountType = value
	@property
	def length_axis3(self) -> LengthAxis3:
		return LengthAxis3(self._instance.LengthAxis3)
	@length_axis3.setter
	def length_axis3(self, value: LengthAxis3):
		self._instance.LengthAxis3 = value
	@property
	def diameter_axis3(self) -> DiameterAxis3:
		return DiameterAxis3(self._instance.DiameterAxis3)
	@diameter_axis3.setter
	def diameter_axis3(self, value: DiameterAxis3):
		self._instance.DiameterAxis3 = value
