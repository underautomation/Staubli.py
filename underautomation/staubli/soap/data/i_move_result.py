import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
from UnderAutomation.Staubli.Soap.Data import IMoveResult as i_move_result
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class IMoveResult:
	'''Represents the result of a robot motion command.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_move_result()
		else:
			self._instance = _internal

	@property
	def id(self) -> int:
		'''Identifier of the motion command.'''
		return self._instance.Id

	@property
	def return_code(self) -> MotionReturnCode:
		'''Return code indicating the outcome of the motion command.'''
		return MotionReturnCode(int(self._instance.ReturnCode))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IMoveResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
