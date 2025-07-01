import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetAllPhysicalIosRequest as get_all_physical_ios_request

class GetAllPhysicalIosRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_all_physical_ios_request()
		else:
			self._instance = _internal
