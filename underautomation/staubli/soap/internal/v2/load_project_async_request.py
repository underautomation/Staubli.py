import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import LoadProjectAsyncRequest as load_project_async_request

class LoadProjectAsyncRequest:
	'''SOAP request to asynchronously load a project on the controller.'''
	def __init__(self, applicationPath: str, _internal = 0):
		'''Initializes a new instance with the specified application path.

		:param applicationPath: Path to the project on the controller.
		'''
		if(_internal == 0):
			self._instance = load_project_async_request(applicationPath)
		else:
			self._instance = _internal

	@property
	def application_path(self) -> str:
		'''Path to the project on the controller.'''
		return self._instance.applicationPath

	@application_path.setter
	def application_path(self, value: str):
		self._instance.applicationPath = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LoadProjectAsyncRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
