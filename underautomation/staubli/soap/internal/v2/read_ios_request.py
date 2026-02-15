import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import ReadIosRequest as read_ios_request

class ReadIosRequest:
	'''SOAP request to read the state of specified physical I/Os.'''
	def __init__(self, ios: typing.List[str], xgetDescription: bool, _internal = 0):
		'''Initializes a new instance with the specified I/O paths and description flag.

		:param ios: Array of physical I/O paths to read.
		:param xgetDescription: Whether to include I/O descriptions in the response.
		'''
		if(_internal == 0):
			self._instance = read_ios_request(ios, xgetDescription)
		else:
			self._instance = _internal

	@property
	def ios(self) -> typing.List[str]:
		'''Array of physical I/O paths to read.'''
		return self._instance.ios

	@ios.setter
	def ios(self, value: typing.List[str]):
		self._instance.ios = value

	@property
	def xget_description(self) -> bool:
		'''Whether to include I/O descriptions in the response.'''
		return self._instance.xgetDescription

	@xget_description.setter
	def xget_description(self, value: bool):
		self._instance.xgetDescription = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReadIosRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
