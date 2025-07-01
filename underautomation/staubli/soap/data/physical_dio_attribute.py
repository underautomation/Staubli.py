import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalDioAttribute as physical_dio_attribute

class PhysicalDioAttribute:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_dio_attribute()
		else:
			self._instance = _internal
	@property
	def inverted(self) -> bool:
		return self._instance.Inverted
	@inverted.setter
	def inverted(self, value: bool):
		self._instance.Inverted = value
