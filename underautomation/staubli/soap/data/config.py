import typing
from underautomation.staubli.soap.data.anthro_config import AnthroConfig
from underautomation.staubli.soap.data.scara_config import ScaraConfig
from underautomation.staubli.soap.data.vrbx_config import VrbxConfig
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Config as config

class Config:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = config()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def anthro_config(self) -> AnthroConfig:
		return AnthroConfig(self._instance.AnthroConfig)
	@anthro_config.setter
	def anthro_config(self, value: AnthroConfig):
		self._instance.AnthroConfig = value._instance if value else None
	@property
	def scara_config(self) -> ScaraConfig:
		return ScaraConfig(self._instance.ScaraConfig)
	@scara_config.setter
	def scara_config(self, value: ScaraConfig):
		self._instance.ScaraConfig = value._instance if value else None
	@property
	def vrbx_config(self) -> VrbxConfig:
		return VrbxConfig(self._instance.VrbxConfig)
	@vrbx_config.setter
	def vrbx_config(self, value: VrbxConfig):
		self._instance.VrbxConfig = value._instance if value else None
