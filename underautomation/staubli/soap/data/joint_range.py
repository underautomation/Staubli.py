import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import JointRange as joint_range

class JointRange:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_range()
		else:
			self._instance = _internal
	@property
	def min(self) -> typing.List[float]:
		return self._instance.Min
	@min.setter
	def min(self, value: typing.List[float]):
		self._instance.Min = value
	@property
	def max(self) -> typing.List[float]:
		return self._instance.Max
	@max.setter
	def max(self, value: typing.List[float]):
		self._instance.Max = value
