import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import GetAllPhysicalIosRequest as get_all_physical_ios_request

class GetAllPhysicalIosRequest:
	'''SOAP request to retrieve all physical I/Os from the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetAllPhysicalIosRequest class.'''
		if(_internal == 0):
			self._instance = get_all_physical_ios_request()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetAllPhysicalIosRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
