import typing
from underautomation.staubli.soap.data.physical_io import PhysicalIo
from UnderAutomation.Staubli.Soap.Internal.V2 import PhysicalIosWrapper as physical_ios_wrapper

class PhysicalIosWrapper:
	'''Wrapper for the array of physical I/Os.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_ios_wrapper()
		else:
			self._instance = _internal

	@property
	def physical_ios(self) -> typing.List[PhysicalIo]:
		'''Array of physical I/Os.'''
		return [PhysicalIo(x) for x in self._instance.PhysicalIos]

	@physical_ios.setter
	def physical_ios(self, value: typing.List[PhysicalIo]):
		self._instance.PhysicalIos = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalIosWrapper):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
