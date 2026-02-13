import typing
from underautomation.staubli.soap.internal.v2.get_all_physical_ios_response_data import GetAllPhysicalIosResponseData
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetAllPhysicalIosResponse as get_all_physical_ios_response

class GetAllPhysicalIosResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_all_physical_ios_response()
		else:
			self._instance = _internal
	@property
	def data(self) -> GetAllPhysicalIosResponseData:
		return GetAllPhysicalIosResponseData(self._instance.Data)
	@data.setter
	def data(self, value: GetAllPhysicalIosResponseData):
		self._instance.Data = value._instance if value else None
