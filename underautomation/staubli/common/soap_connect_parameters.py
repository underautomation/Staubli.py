import typing
from underautomation.staubli.soap.internal.soap_connect_parameters_base import SoapConnectParametersBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Common import SoapConnectParameters as soap_connect_parameters

class SoapConnectParameters(SoapConnectParametersBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_connect_parameters()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value
	@property
	def defaul_t__port(self) -> int:
		return self._instance.DEFAULT_PORT
	@defaul_t__port.setter
	def defaul_t__port(self, value: int):
		self._instance.DEFAULT_PORT = value
