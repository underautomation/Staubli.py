import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import LoadProjectAsyncResponse as load_project_async_response

class LoadProjectAsyncResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = load_project_async_response()
		else:
			self._instance = _internal
