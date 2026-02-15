import typing
from underautomation.staubli.soap.data.anthro_config import AnthroConfig
from underautomation.staubli.soap.data.scara_config import ScaraConfig
from underautomation.staubli.soap.data.vrbx_config import VrbxConfig
from UnderAutomation.Staubli.Soap.Data import Config as config

class Config:
	'''Robot configuration containing kinematic-specific settings.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the Config class.'''
		if(_internal == 0):
			self._instance = config()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def anthro_config(self) -> AnthroConfig:
		'''Anthropomorphic robot configuration.'''
		return AnthroConfig(self._instance.AnthroConfig)

	@anthro_config.setter
	def anthro_config(self, value: AnthroConfig):
		self._instance.AnthroConfig = value._instance if value else None

	@property
	def scara_config(self) -> ScaraConfig:
		'''SCARA robot configuration.'''
		return ScaraConfig(self._instance.ScaraConfig)

	@scara_config.setter
	def scara_config(self, value: ScaraConfig):
		self._instance.ScaraConfig = value._instance if value else None

	@property
	def vrbx_config(self) -> VrbxConfig:
		'''VRBX robot configuration.'''
		return VrbxConfig(self._instance.VrbxConfig)

	@vrbx_config.setter
	def vrbx_config(self, value: VrbxConfig):
		self._instance.VrbxConfig = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Config):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
