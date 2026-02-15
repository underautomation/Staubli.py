import typing
from UnderAutomation.Staubli.Soap.Internal.V0 import LogoutResponse as logout_response

class LogoutResponse:
	'''SOAP response for the logout operation.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = logout_response()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LogoutResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
