import typing
from underautomation.staubli.soap.internal.soap_client_base import SoapClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap import SoapClient as soap_client

class SoapClient(SoapClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_client()
		else:
			self._instance = _internal
	def connect(self, ip: str, user: str, password: str, port: int) -> None:
		self._instance.Connect(ip, user, password, port)
