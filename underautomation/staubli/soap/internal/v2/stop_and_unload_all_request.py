import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import StopAndUnloadAllRequest as stop_and_unload_all_request

class StopAndUnloadAllRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = stop_and_unload_all_request()
		else:
			self._instance = _internal
