import typing
from UnderAutomation.Staubli.Soap.Internal.V0 import GetControllerParametersRequest as get_controller_parameters_request

class GetControllerParametersRequest:
	'''SOAP request to retrieve the controller parameters.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetControllerParametersRequest class.'''
		if(_internal == 0):
			self._instance = get_controller_parameters_request()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetControllerParametersRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
