import typing
from underautomation.staubli.common.soap_connect_parameters import SoapConnectParameters
from UnderAutomation.Staubli import ConnectionParameters as connection_parameters

class ConnectionParameters:
	'''Connection parameters'''
	def __init__(self, address: str, _internal = 0):
		'''Instanciate a new connection parameters with a specified address'''
		if(_internal == 0):
			self._instance = connection_parameters(address)
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def address(self) -> str:
		'''Address of the robot (IP or host name)'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def ping_before_connect(self) -> bool:
		'''Send a ping command before initializing any connections'''
		return self._instance.PingBeforeConnect

	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value

	@property
	def soap(self) -> SoapConnectParameters:
		'''Soap connection parameters'''
		return SoapConnectParameters(self._instance.Soap)

	@soap.setter
	def soap(self, value: SoapConnectParameters):
		self._instance.Soap = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectionParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
