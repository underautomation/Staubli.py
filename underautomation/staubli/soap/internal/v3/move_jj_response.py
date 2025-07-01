import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveJJResponse as move_jj_response

class MoveJJResponse:
	def __init__(self, id: int, motRet: MotionReturnCode, _internal = 0):
		if(_internal == 0):
			self._instance = move_jj_response(id, motRet)
		else:
			self._instance = _internal
	@property
	def id(self) -> int:
		return self._instance.Id
	@id.setter
	def id(self, value: int):
		self._instance.Id = value
	@property
	def return_code(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.ReturnCode)
	@return_code.setter
	def return_code(self, value: MotionReturnCode):
		self._instance.ReturnCode = value
