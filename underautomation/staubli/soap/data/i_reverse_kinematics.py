import typing
from underautomation.staubli.soap.data.reversing_result import ReversingResult
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import IReverseKinematics as i_reverse_kinematics

class IReverseKinematics:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_reverse_kinematics()
		else:
			self._instance = _internal
	@property
	def joint(self) -> typing.List[float]:
		return self._instance.Joint
	@property
	def result(self) -> ReversingResult:
		return ReversingResult(self._instance.Result)
