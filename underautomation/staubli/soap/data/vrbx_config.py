import typing
from underautomation.staubli.soap.data.above_below_config import AboveBelowConfig
from underautomation.staubli.soap.data.positive_negative_config import PositiveNegativeConfig
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import VrbxConfig as vrbx_config

class VrbxConfig:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vrbx_config()
		else:
			self._instance = _internal
	@property
	def joint1(self) -> AboveBelowConfig:
		return AboveBelowConfig(self._instance.Joint1)
	@joint1.setter
	def joint1(self, value: AboveBelowConfig):
		self._instance.Joint1 = value
	@property
	def joint3(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Joint3)
	@joint3.setter
	def joint3(self, value: PositiveNegativeConfig):
		self._instance.Joint3 = value
	@property
	def joint5(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Joint5)
	@joint5.setter
	def joint5(self, value: PositiveNegativeConfig):
		self._instance.Joint5 = value
