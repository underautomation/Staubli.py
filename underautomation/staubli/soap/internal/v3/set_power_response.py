import typing
from underautomation.staubli.soap.data.power_return_code import PowerReturnCode
from UnderAutomation.Staubli.Soap.Internal.V3 import SetPowerResponse as set_power_response
from UnderAutomation.Staubli.Soap.Data import PowerReturnCode as power_return_code

class SetPowerResponse:
	'''SOAP response for the set power operation.'''
	def __init__(self, code: PowerReturnCode, _internal = 0):
		'''Initializes a new instance with the specified return code.

		:param code: Power operation return code.
		'''
		if(_internal == 0):
			self._instance = set_power_response(code)
		else:
			self._instance = _internal

	@property
	def code(self) -> PowerReturnCode:
		'''Return code indicating the outcome of the power operation.'''
		return PowerReturnCode(int(self._instance.code))

	@code.setter
	def code(self, value: PowerReturnCode):
		self._instance.code = power_return_code(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetPowerResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
