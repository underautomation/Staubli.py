import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import LoginResponse as login_response

class LoginResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = login_response()
		else:
			self._instance = _internal
	@property
	def sid(self) -> int:
		return self._instance.Sid
	@sid.setter
	def sid(self, value: int):
		self._instance.Sid = value
