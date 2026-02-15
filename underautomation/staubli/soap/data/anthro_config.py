import typing
from underautomation.staubli.soap.data.shoulder_config import ShoulderConfig
from underautomation.staubli.soap.data.positive_negative_config import PositiveNegativeConfig
from UnderAutomation.Staubli.Soap.Data import AnthroConfig as anthro_config
from UnderAutomation.Staubli.Soap.Data import ShoulderConfig as shoulder_config
from UnderAutomation.Staubli.Soap.Data import PositiveNegativeConfig as positive_negative_config

class AnthroConfig:
	'''Configuration for an anthropomorphic robot (shoulder, elbow, wrist).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the AnthroConfig class.'''
		if(_internal == 0):
			self._instance = anthro_config()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def shoulder(self) -> ShoulderConfig:
		'''Shoulder configuration.'''
		return ShoulderConfig(int(self._instance.Shoulder))

	@shoulder.setter
	def shoulder(self, value: ShoulderConfig):
		self._instance.Shoulder = shoulder_config(int(value))

	@property
	def elbow(self) -> PositiveNegativeConfig:
		'''Elbow configuration.'''
		return PositiveNegativeConfig(int(self._instance.Elbow))

	@elbow.setter
	def elbow(self, value: PositiveNegativeConfig):
		self._instance.Elbow = positive_negative_config(int(value))

	@property
	def wrist(self) -> PositiveNegativeConfig:
		'''Wrist configuration.'''
		return PositiveNegativeConfig(int(self._instance.Wrist))

	@wrist.setter
	def wrist(self, value: PositiveNegativeConfig):
		self._instance.Wrist = positive_negative_config(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AnthroConfig):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
