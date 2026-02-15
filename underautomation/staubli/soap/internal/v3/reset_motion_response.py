import typing
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
from UnderAutomation.Staubli.Soap.Internal.V3 import ResetMotionResponse as reset_motion_response
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class ResetMotionResponse:
	'''SOAP response for motion control operations (reset, restart, stop).'''
	def __init__(self, motRet: MotionReturnCode, _internal = 0):
		'''Initializes a new instance with the specified return code.

		:param motRet: Motion return code.
		'''
		if(_internal == 0):
			self._instance = reset_motion_response(motRet)
		else:
			self._instance = _internal

	@property
	def return_code(self) -> MotionReturnCode:
		'''Return code indicating the outcome of the motion operation.'''
		return MotionReturnCode(int(self._instance.ReturnCode))

	@return_code.setter
	def return_code(self, value: MotionReturnCode):
		self._instance.ReturnCode = motion_return_code(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ResetMotionResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
