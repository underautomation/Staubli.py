import typing
from UnderAutomation.Staubli.Soap.Internal.V0 import LoginResponse as login_response

class LoginResponse:
	'''SOAP response containing the session identifier after login.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = login_response()
		else:
			self._instance = _internal

	@property
	def sid(self) -> int:
		'''Session identifier assigned by the controller.'''
		return self._instance.Sid

	@sid.setter
	def sid(self, value: int):
		self._instance.Sid = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LoginResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
