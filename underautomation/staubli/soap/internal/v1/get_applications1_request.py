import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V1 import GetApplications1Request as get_applications1_request

class GetApplications1Request:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_applications1_request()
		else:
			self._instance = _internal
