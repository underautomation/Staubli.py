import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import IMoveResult as i_move_result
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class IMoveResult:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_move_result()
		else:
			self._instance = _internal
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def return_code(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.ReturnCode)
