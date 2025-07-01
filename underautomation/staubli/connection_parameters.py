import typing
from underautomation.staubli.common.soap_connect_parameters import SoapConnectParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__),  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli import ConnectionParameters as connection_parameters

class ConnectionParameters:
	def __init__(self, address: str, _internal = 0):
		if(_internal == 0):
			self._instance = connection_parameters(address)
		else:
			self._instance = _internal
	@property
	def address(self) -> str:
		return self._instance.Address
	@address.setter
	def address(self, value: str):
		self._instance.Address = value
	@property
	def ping_before_connect(self) -> bool:
		return self._instance.PingBeforeConnect
	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value
	@property
	def soap(self) -> SoapConnectParameters:
		return SoapConnectParameters(self._instance.Soap)
	@soap.setter
	def soap(self, value: SoapConnectParameters):
		self._instance.Soap = value
