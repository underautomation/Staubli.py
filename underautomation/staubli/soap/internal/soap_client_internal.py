import typing
from underautomation.staubli.soap.internal.soap_client_base import SoapClientBase
from UnderAutomation.Staubli.Soap.Internal import SoapClientInternal as soap_client_internal

class SoapClientInternal(SoapClientBase):
	'''Internal class for SOAP client, do not use directly'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SoapClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
