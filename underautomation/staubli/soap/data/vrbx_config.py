import typing
from underautomation.staubli.soap.data.above_below_config import AboveBelowConfig
from underautomation.staubli.soap.data.positive_negative_config import PositiveNegativeConfig
from UnderAutomation.Staubli.Soap.Data import VrbxConfig as vrbx_config
from UnderAutomation.Staubli.Soap.Data import AboveBelowConfig as above_below_config
from UnderAutomation.Staubli.Soap.Data import PositiveNegativeConfig as positive_negative_config

class VrbxConfig:
	'''Configuration for a VRBX-type robot.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the VrbxConfig class.'''
		if(_internal == 0):
			self._instance = vrbx_config()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def joint1(self) -> AboveBelowConfig:
		'''Joint 1 above/below configuration.'''
		return AboveBelowConfig(int(self._instance.Joint1))

	@joint1.setter
	def joint1(self, value: AboveBelowConfig):
		self._instance.Joint1 = above_below_config(int(value))

	@property
	def joint3(self) -> PositiveNegativeConfig:
		'''Joint 3 positive/negative configuration.'''
		return PositiveNegativeConfig(int(self._instance.Joint3))

	@joint3.setter
	def joint3(self, value: PositiveNegativeConfig):
		self._instance.Joint3 = positive_negative_config(int(value))

	@property
	def joint5(self) -> PositiveNegativeConfig:
		'''Joint 5 positive/negative configuration.'''
		return PositiveNegativeConfig(int(self._instance.Joint5))

	@joint5.setter
	def joint5(self, value: PositiveNegativeConfig):
		self._instance.Joint5 = positive_negative_config(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VrbxConfig):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
