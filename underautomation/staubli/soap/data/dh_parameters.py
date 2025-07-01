import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import DhParameters as dh_parameters

class DhParameters:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dh_parameters()
		else:
			self._instance = _internal
	@property
	def theta(self) -> float:
		return self._instance.Theta
	@theta.setter
	def theta(self, value: float):
		self._instance.Theta = value
	@property
	def d(self) -> float:
		return self._instance.D
	@d.setter
	def d(self, value: float):
		self._instance.D = value
	@property
	def a(self) -> float:
		return self._instance.A
	@a.setter
	def a(self, value: float):
		self._instance.A = value
	@property
	def alpha(self) -> float:
		return self._instance.Alpha
	@alpha.setter
	def alpha(self, value: float):
		self._instance.Alpha = value
	@property
	def beta(self) -> float:
		return self._instance.Beta
	@beta.setter
	def beta(self, value: float):
		self._instance.Beta = value
