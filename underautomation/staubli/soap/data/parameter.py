import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Parameter as parameter

class Parameter:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = parameter()
		else:
			self._instance = _internal
	@property
	def key(self) -> str:
		return self._instance.Key
	@key.setter
	def key(self, value: str):
		self._instance.Key = value
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def value(self) -> str:
		return self._instance.Value
	@value.setter
	def value(self, value: str):
		self._instance.Value = value
