import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ResetMotionResponse as reset_motion_response
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class ResetMotionResponse:
	def __init__(self, motRet: MotionReturnCode, _internal = 0):
		if(_internal == 0):
			self._instance = reset_motion_response(motRet)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def return_code(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.ReturnCode)
	@return_code.setter
	def return_code(self, value: MotionReturnCode):
		self._instance.ReturnCode = motion_return_code(int(value))
