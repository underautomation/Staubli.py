import typing
from underautomation.staubli.soap.errors.soap_error_code import SoapErrorCode
from UnderAutomation.Staubli.Soap.Errors import CustomSoapException as custom_soap_exception
from UnderAutomation.Staubli.Soap.Errors import SoapErrorCode as soap_error_code

class CustomSoapException:
	'''Custom exception class for handling SOAP errors with specific error codes and descriptions.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = custom_soap_exception()
		else:
			self._instance = _internal

	@property
	def error_code_text(self) -> str:
		'''The error code text as received from the SOAP response, formatted as a kebab-case string.'''
		return self._instance.ErrorCodeText

	@property
	def error_code(self) -> SoapErrorCode:
		'''The error code as an enum value, parsed from the ErrorCodeText.'''
		return SoapErrorCode(int(self._instance.ErrorCode))

	@property
	def description(self) -> str:
		'''A human-readable description of the error, providing additional context about the failure.'''
		return self._instance.Description

	@property
	def message(self) -> str:
		'''Gets the error message that describes the current exception.'''
		return self._instance.Message

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CustomSoapException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
