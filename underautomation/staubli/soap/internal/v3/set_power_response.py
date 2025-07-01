import typing
from underautomation.staubli.soap.data.power_return_code import PowerReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import SetPowerResponse as set_power_response

class SetPowerResponse:
	def __init__(self, code: PowerReturnCode, _internal = 0):
		if(_internal == 0):
			self._instance = set_power_response(code)
		else:
			self._instance = _internal
	@property
	def code(self) -> PowerReturnCode:
		return PowerReturnCode(self._instance.code)
	@code.setter
	def code(self, value: PowerReturnCode):
		self._instance.code = value
