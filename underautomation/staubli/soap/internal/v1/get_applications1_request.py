import typing
from UnderAutomation.Staubli.Soap.Internal.V1 import GetApplications1Request as get_applications1_request

class GetApplications1Request:
	'''SOAP request to retrieve all VAL applications from the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetApplications1Request class.'''
		if(_internal == 0):
			self._instance = get_applications1_request()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetApplications1Request):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
