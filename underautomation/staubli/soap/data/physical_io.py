import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIo as physical_io

class PhysicalIo:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_io()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def description(self) -> str:
		return self._instance.Description
	@description.setter
	def description(self, value: str):
		self._instance.Description = value
	@property
	def type_str(self) -> str:
		return self._instance.TypeStr
	@type_str.setter
	def type_str(self, value: str):
		self._instance.TypeStr = value
	@property
	def lockable(self) -> bool:
		return self._instance.Lockable
	@lockable.setter
	def lockable(self, value: bool):
		self._instance.Lockable = value
