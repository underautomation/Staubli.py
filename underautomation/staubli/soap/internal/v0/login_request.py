import typing
from UnderAutomation.Staubli.Soap.Internal.V0 import LoginRequest as login_request

class LoginRequest:
	'''SOAP request to log in to the controller.'''
	def __init__(self, user: str, pwd: str, _internal = 0):
		'''Initializes a new instance with the specified credentials.

		:param user: Username.
		:param pwd: Password.
		'''
		if(_internal == 0):
			self._instance = login_request(user, pwd)
		else:
			self._instance = _internal

	@property
	def user(self) -> str:
		'''Username for authentication.'''
		return self._instance.user

	@user.setter
	def user(self, value: str):
		self._instance.user = value

	@property
	def pwd(self) -> str:
		'''Password for authentication.'''
		return self._instance.pwd

	@pwd.setter
	def pwd(self, value: str):
		self._instance.pwd = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LoginRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
