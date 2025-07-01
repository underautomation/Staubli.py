import typing
from underautomation.staubli.soap.data.shoulder_config import ShoulderConfig
from underautomation.staubli.soap.data.positive_negative_config import PositiveNegativeConfig
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import AnthroConfig as anthro_config

class AnthroConfig:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = anthro_config()
		else:
			self._instance = _internal
	@property
	def shoulder(self) -> ShoulderConfig:
		return ShoulderConfig(self._instance.Shoulder)
	@shoulder.setter
	def shoulder(self, value: ShoulderConfig):
		self._instance.Shoulder = value
	@property
	def elbow(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Elbow)
	@elbow.setter
	def elbow(self, value: PositiveNegativeConfig):
		self._instance.Elbow = value
	@property
	def wrist(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Wrist)
	@wrist.setter
	def wrist(self, value: PositiveNegativeConfig):
		self._instance.Wrist = value
