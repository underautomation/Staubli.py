import typing
from underautomation.staubli.soap.data.physical_io import PhysicalIo
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import PhysicalIosWrapper as physical_ios_wrapper

class PhysicalIosWrapper:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_ios_wrapper()
		else:
			self._instance = _internal
	@property
	def physical_ios(self) -> typing.List[PhysicalIo]:
		return [PhysicalIo(x) for x in self._instance.PhysicalIos]
	@physical_ios.setter
	def physical_ios(self, value: typing.List[PhysicalIo]):
		self._instance.PhysicalIos = value
