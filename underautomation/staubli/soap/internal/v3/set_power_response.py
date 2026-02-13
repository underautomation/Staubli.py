import typing
from underautomation.staubli.soap.data.power_return_code import PowerReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import SetPowerResponse as set_power_response
from UnderAutomation.Staubli.Soap.Data import PowerReturnCode as power_return_code

class SetPowerResponse:
	def __init__(self, code: PowerReturnCode, _internal = 0):
		if(_internal == 0):
			self._instance = set_power_response(code)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def code(self) -> PowerReturnCode:
		return PowerReturnCode(self._instance.code)
	@code.setter
	def code(self, value: PowerReturnCode):
		self._instance.code = power_return_code(int(value))
