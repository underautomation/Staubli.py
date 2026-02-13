import typing
from underautomation.staubli.soap.data.shoulder_config import ShoulderConfig
from underautomation.staubli.soap.data.positive_negative_config import PositiveNegativeConfig
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import AnthroConfig as anthro_config
from UnderAutomation.Staubli.Soap.Data import ShoulderConfig as shoulder_config
from UnderAutomation.Staubli.Soap.Data import PositiveNegativeConfig as positive_negative_config

class AnthroConfig:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = anthro_config()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def shoulder(self) -> ShoulderConfig:
		return ShoulderConfig(self._instance.Shoulder)
	@shoulder.setter
	def shoulder(self, value: ShoulderConfig):
		self._instance.Shoulder = shoulder_config(int(value))
	@property
	def elbow(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Elbow)
	@elbow.setter
	def elbow(self, value: PositiveNegativeConfig):
		self._instance.Elbow = positive_negative_config(int(value))
	@property
	def wrist(self) -> PositiveNegativeConfig:
		return PositiveNegativeConfig(self._instance.Wrist)
	@wrist.setter
	def wrist(self, value: PositiveNegativeConfig):
		self._instance.Wrist = positive_negative_config(int(value))
