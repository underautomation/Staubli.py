import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import StopApplicationResponse as stop_application_response

class StopApplicationResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stop_application_response()
		else:
			self._instance = _internal
