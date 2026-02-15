import typing
from UnderAutomation.Staubli.Soap.Internal import SoapConnectParametersBase as soap_connect_parameters_base

class SoapConnectParametersBase:
	'''Base class for SOAP connection parameters'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def user(self) -> str:
		'''Username for the SOAP service (default: default)'''
		return self._instance.User

	@user.setter
	def user(self, value: str):
		self._instance.User = value

	@property
	def password(self) -> str:
		'''Password for the SOAP service (default: default)'''
		return self._instance.Password

	@password.setter
	def password(self, value: str):
		self._instance.Password = value

	@property
	def port(self) -> int:
		'''Port of the SOAP service (default: 851)'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SoapConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
