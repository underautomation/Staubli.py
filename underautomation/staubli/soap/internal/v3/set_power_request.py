import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import SetPowerRequest as set_power_request

class SetPowerRequest:
	def __init__(self, power: bool, _internal = 0):
		if(_internal == 0):
			self._instance = set_power_request(power)
		else:
			self._instance = _internal
	@property
	def power(self) -> bool:
		return self._instance.power
	@power.setter
	def power(self, value: bool):
		self._instance.power = value
