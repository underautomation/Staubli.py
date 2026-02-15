import typing
from underautomation.staubli.soap.data.val_application import ValApplication
from UnderAutomation.Staubli.Soap.Internal.V1 import GetApplications1Response as get_applications1_response

class GetApplications1Response:
	'''SOAP response containing the list of VAL applications.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetApplications1Response class.'''
		if(_internal == 0):
			self._instance = get_applications1_response()
		else:
			self._instance = _internal

	@property
	def applications(self) -> typing.List[ValApplication]:
		'''Array of VAL applications available on the controller.'''
		return [ValApplication(x) for x in self._instance.Applications]

	@applications.setter
	def applications(self, value: typing.List[ValApplication]):
		self._instance.Applications = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetApplications1Response):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
