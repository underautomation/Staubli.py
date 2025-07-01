import typing
from underautomation.staubli.soap.errors.soap_error_code import SoapErrorCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Errors import CustomSoapException as custom_soap_exception

class CustomSoapException:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = custom_soap_exception()
		else:
			self._instance = _internal
	@property
	def error_code_text(self) -> str:
		return self._instance.ErrorCodeText
	@property
	def error_code(self) -> SoapErrorCode:
		return SoapErrorCode(self._instance.ErrorCode)
	@property
	def description(self) -> str:
		return self._instance.Description
	@property
	def message(self) -> str:
		return self._instance.Message
