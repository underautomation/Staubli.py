import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import StopApplicationResponse as stop_application_response

class StopApplicationResponse:
	'''SOAP response for the stop application operation.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the StopApplicationResponse class.'''
		if(_internal == 0):
			self._instance = stop_application_response()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StopApplicationResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
