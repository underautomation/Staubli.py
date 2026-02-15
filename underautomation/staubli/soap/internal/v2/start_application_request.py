import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import StartApplicationRequest as start_application_request

class StartApplicationRequest:
	'''SOAP request to start a VAL application on the controller.'''
	def __init__(self, applicationPath: str, _internal = 0):
		'''Initializes a new instance with the specified application path.

		:param applicationPath: Application path on the controller.
		'''
		if(_internal == 0):
			self._instance = start_application_request(applicationPath)
		else:
			self._instance = _internal

	@property
	def application_path(self) -> str:
		'''Application path on the controller.'''
		return self._instance.applicationPath

	@application_path.setter
	def application_path(self, value: str):
		self._instance.applicationPath = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StartApplicationRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
