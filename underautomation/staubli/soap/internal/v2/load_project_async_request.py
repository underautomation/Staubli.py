import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import LoadProjectAsyncRequest as load_project_async_request

class LoadProjectAsyncRequest:
	def __init__(self, applicationPath: str, _internal = 0):
		if(_internal == 0):
			self._instance = load_project_async_request(applicationPath)
		else:
			self._instance = _internal
	@property
	def application_path(self) -> str:
		return self._instance.applicationPath
	@application_path.setter
	def application_path(self, value: str):
		self._instance.applicationPath = value
