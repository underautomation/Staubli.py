import typing
from underautomation.staubli.soap.data.shoulder_config import ShoulderConfig
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ScaraConfig as scara_config

class ScaraConfig:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = scara_config()
		else:
			self._instance = _internal
	@property
	def shoulder(self) -> ShoulderConfig:
		return ShoulderConfig(self._instance.Shoulder)
	@shoulder.setter
	def shoulder(self, value: ShoulderConfig):
		self._instance.Shoulder = value
