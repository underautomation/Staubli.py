import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ResetMotionResponse as reset_motion_response

class ResetMotionResponse:
	def __init__(self, motRet: MotionReturnCode, _internal = 0):
		if(_internal == 0):
			self._instance = reset_motion_response(motRet)
		else:
			self._instance = _internal
	@property
	def mot_ret(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.motRet)
	@mot_ret.setter
	def mot_ret(self, value: MotionReturnCode):
		self._instance.motRet = value
