import typing
from underautomation.staubli.soap.internal.v2.physical_ios_wrapper import PhysicalIosWrapper
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetAllPhysicalIosResponseData as get_all_physical_ios_response_data

class GetAllPhysicalIosResponseData:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_all_physical_ios_response_data()
		else:
			self._instance = _internal
	@property
	def data(self) -> PhysicalIosWrapper:
		return PhysicalIosWrapper(self._instance.Data)
	@data.setter
	def data(self, value: PhysicalIosWrapper):
		self._instance.Data = value._instance if value else None
