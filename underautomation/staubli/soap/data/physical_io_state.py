import typing
from underautomation.staubli.soap.data.physical_io_enum_state import PhysicalIoEnumState
from underautomation.staubli.soap.data.physical_io_attribute import PhysicalIoAttribute
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIoState as physical_io_state

class PhysicalIoState:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_io_state()
		else:
			self._instance = _internal
	@property
	def state(self) -> PhysicalIoEnumState:
		return PhysicalIoEnumState(self._instance.State)
	@state.setter
	def state(self, value: PhysicalIoEnumState):
		self._instance.State = value
	@property
	def locked(self) -> bool:
		return self._instance.Locked
	@locked.setter
	def locked(self, value: bool):
		self._instance.Locked = value
	@property
	def simulated(self) -> bool:
		return self._instance.Simulated
	@simulated.setter
	def simulated(self, value: bool):
		self._instance.Simulated = value
	@property
	def value(self) -> float:
		return self._instance.Value
	@value.setter
	def value(self, value: float):
		self._instance.Value = value
	@property
	def attribute(self) -> PhysicalIoAttribute:
		return PhysicalIoAttribute(self._instance.Attribute)
	@attribute.setter
	def attribute(self, value: PhysicalIoAttribute):
		self._instance.Attribute = value
