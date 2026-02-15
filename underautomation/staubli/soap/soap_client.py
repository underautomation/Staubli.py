import typing
from underautomation.staubli.soap.internal.soap_client_base import SoapClientBase
from UnderAutomation.Staubli.Soap import SoapClient as soap_client

class SoapClient(SoapClientBase):
	'''SOAP client for Staubli robots'''
	def __init__(self, _internal = 0):
		'''Create a new instance of SoapClient'''
		if(_internal == 0):
			self._instance = soap_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, user: str, password: str, port: int) -> None:
		'''Connect to a robot

		:param ip: IP or network name of the robot
		:param user: Username for the SOAP service
		:param password: Password for the SOAP service
		:param port: Port of the SOAP service
		'''
		self._instance.Connect(ip, user, password, port)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SoapClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
