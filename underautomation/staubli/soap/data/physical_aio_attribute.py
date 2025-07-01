import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalAioAttribute as physical_aio_attribute

class PhysicalAioAttribute:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_aio_attribute()
		else:
			self._instance = _internal
	@property
	def coefficient_a(self) -> float:
		return self._instance.CoefficientA
	@coefficient_a.setter
	def coefficient_a(self, value: float):
		self._instance.CoefficientA = value
	@property
	def coefficient_b(self) -> float:
		return self._instance.CoefficientB
	@coefficient_b.setter
	def coefficient_b(self, value: float):
		self._instance.CoefficientB = value
