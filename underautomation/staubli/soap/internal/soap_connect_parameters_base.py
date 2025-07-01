import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal import SoapConnectParametersBase as soap_connect_parameters_base

class SoapConnectParametersBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_connect_parameters_base()
		else:
			self._instance = _internal
	@property
	def user(self) -> str:
		return self._instance.User
	@user.setter
	def user(self, value: str):
		self._instance.User = value
	@property
	def password(self) -> str:
		return self._instance.Password
	@password.setter
	def password(self, value: str):
		self._instance.Password = value
	@property
	def port(self) -> int:
		return self._instance.Port
	@port.setter
	def port(self, value: int):
		self._instance.Port = value
