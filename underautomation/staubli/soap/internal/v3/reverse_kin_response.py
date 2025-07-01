import typing
from underautomation.staubli.soap.data.reversing_result import ReversingResult
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ReverseKinResponse as reverse_kin_response

class ReverseKinResponse:
	def __init__(self, jointOut: typing.List[float], reversingResult: ReversingResult, _internal = 0):
		if(_internal == 0):
			self._instance = reverse_kin_response(jointOut, reversingResult)
		else:
			self._instance = _internal
	@property
	def joint(self) -> typing.List[float]:
		return self._instance.Joint
	@joint.setter
	def joint(self, value: typing.List[float]):
		self._instance.Joint = value
	@property
	def result(self) -> ReversingResult:
		return ReversingResult(self._instance.Result)
	@result.setter
	def result(self, value: ReversingResult):
		self._instance.Result = value
