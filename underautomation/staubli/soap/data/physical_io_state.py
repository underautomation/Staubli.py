import typing
from underautomation.staubli.soap.data.physical_io_enum_state import PhysicalIoEnumState
from underautomation.staubli.soap.data.physical_io_attribute import PhysicalIoAttribute
from UnderAutomation.Staubli.Soap.Data import PhysicalIoState as physical_io_state
from UnderAutomation.Staubli.Soap.Data import PhysicalIoEnumState as physical_io_enum_state

class PhysicalIoState:
	'''Current state and value of a physical I/O.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PhysicalIoState class.'''
		if(_internal == 0):
			self._instance = physical_io_state()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def state(self) -> PhysicalIoEnumState:
		'''Definition state of the I/O.'''
		return PhysicalIoEnumState(int(self._instance.State))

	@state.setter
	def state(self, value: PhysicalIoEnumState):
		self._instance.State = physical_io_enum_state(int(value))

	@property
	def locked(self) -> bool:
		'''Indicates whether the I/O is locked.'''
		return self._instance.Locked

	@locked.setter
	def locked(self, value: bool):
		self._instance.Locked = value

	@property
	def simulated(self) -> bool:
		'''Indicates whether the I/O is in simulation mode.'''
		return self._instance.Simulated

	@simulated.setter
	def simulated(self, value: bool):
		self._instance.Simulated = value

	@property
	def value(self) -> float:
		'''Current numeric value of the I/O.'''
		return self._instance.Value

	@value.setter
	def value(self, value: float):
		self._instance.Value = value

	@property
	def attribute(self) -> PhysicalIoAttribute:
		'''I/O type-specific attributes (analog or digital).'''
		return PhysicalIoAttribute(self._instance.Attribute)

	@attribute.setter
	def attribute(self, value: PhysicalIoAttribute):
		self._instance.Attribute = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalIoState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
