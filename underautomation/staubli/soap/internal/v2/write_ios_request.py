import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import WriteIosRequest as write_ios_request

class WriteIosRequest:
	def __init__(self, ios: typing.List[str], values: typing.List[float], _internal = 0):
		if(_internal == 0):
			self._instance = write_ios_request(ios, values)
		else:
			self._instance = _internal
	@property
	def ios(self) -> typing.List[str]:
		return self._instance.ios
	@ios.setter
	def ios(self, value: typing.List[str]):
		self._instance.ios = value
	@property
	def values(self) -> typing.List[float]:
		return self._instance.values
	@values.setter
	def values(self, value: typing.List[float]):
		self._instance.values = value
