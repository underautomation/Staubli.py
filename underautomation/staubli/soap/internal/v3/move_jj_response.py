import typing
from underautomation.staubli.soap.data.i_move_result import IMoveResult
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveJJResponse as move_jj_response
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class MoveJJResponse(IMoveResult):
	'''SOAP response for a motion command, containing the result code.'''
	def __init__(self, id: int, motRet: MotionReturnCode, _internal = 0):
		'''Initializes a new instance with the specified motion identifier and return code.

		:param id: Motion command identifier.
		:param motRet: Motion return code.
		'''
		if(_internal == 0):
			self._instance = move_jj_response(id, motRet)
		else:
			self._instance = _internal

	@property
	def id(self) -> int:
		'''Motion command identifier.'''
		return self._instance.Id

	@id.setter
	def id(self, value: int):
		self._instance.Id = value

	@property
	def return_code(self) -> MotionReturnCode:
		'''Return code indicating the outcome of the motion.'''
		return MotionReturnCode(int(self._instance.ReturnCode))

	@return_code.setter
	def return_code(self, value: MotionReturnCode):
		self._instance.ReturnCode = motion_return_code(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MoveJJResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
