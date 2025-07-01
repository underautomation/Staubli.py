import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import LoginRequest as login_request

class LoginRequest:
	def __init__(self, user: str, pwd: str, _internal = 0):
		if(_internal == 0):
			self._instance = login_request(user, pwd)
		else:
			self._instance = _internal
	@property
	def user(self) -> str:
		return self._instance.user
	@user.setter
	def user(self, value: str):
		self._instance.user = value
	@property
	def pwd(self) -> str:
		return self._instance.pwd
	@pwd.setter
	def pwd(self, value: str):
		self._instance.pwd = value
