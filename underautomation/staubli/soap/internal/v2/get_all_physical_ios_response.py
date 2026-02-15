import typing
from underautomation.staubli.soap.internal.v2.get_all_physical_ios_response_data import GetAllPhysicalIosResponseData
from UnderAutomation.Staubli.Soap.Internal.V2 import GetAllPhysicalIosResponse as get_all_physical_ios_response

class GetAllPhysicalIosResponse:
	'''SOAP response containing all physical I/Os.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_all_physical_ios_response()
		else:
			self._instance = _internal

	@property
	def data(self) -> GetAllPhysicalIosResponseData:
		'''Nested data wrapper for the physical I/Os response.'''
		return GetAllPhysicalIosResponseData(self._instance.Data)

	@data.setter
	def data(self, value: GetAllPhysicalIosResponseData):
		self._instance.Data = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetAllPhysicalIosResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
