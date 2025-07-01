import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import ReadIosRequest as read_ios_request

class ReadIosRequest:
	def __init__(self, ios: typing.List[str], xgetDescription: bool, _internal = 0):
		if(_internal == 0):
			self._instance = read_ios_request(ios, xgetDescription)
		else:
			self._instance = _internal
	@property
	def ios(self) -> typing.List[str]:
		return self._instance.ios
	@ios.setter
	def ios(self, value: typing.List[str]):
		self._instance.ios = value
	@property
	def xget_description(self) -> bool:
		return self._instance.xgetDescription
	@xget_description.setter
	def xget_description(self, value: bool):
		self._instance.xgetDescription = value
