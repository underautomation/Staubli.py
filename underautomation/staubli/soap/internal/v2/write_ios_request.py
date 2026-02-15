import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import WriteIosRequest as write_ios_request

class WriteIosRequest:
	'''SOAP request to write values to specified physical I/Os.'''
	def __init__(self, ios: typing.List[str], values: typing.List[float], _internal = 0):
		'''Initializes a new instance with the specified I/O paths and values.

		:param ios: Array of physical I/O paths to write.
		:param values: Array of values to write.
		'''
		if(_internal == 0):
			self._instance = write_ios_request(ios, values)
		else:
			self._instance = _internal

	@property
	def ios(self) -> typing.List[str]:
		'''Array of physical I/O paths to write.'''
		return self._instance.ios

	@ios.setter
	def ios(self, value: typing.List[str]):
		self._instance.ios = value

	@property
	def values(self) -> typing.List[float]:
		'''Array of values to write to the I/Os.'''
		return self._instance.values

	@values.setter
	def values(self, value: typing.List[float]):
		self._instance.values = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, WriteIosRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
