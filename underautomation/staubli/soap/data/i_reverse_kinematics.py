import typing
from underautomation.staubli.soap.data.reversing_result import ReversingResult
from UnderAutomation.Staubli.Soap.Data import IReverseKinematics as i_reverse_kinematics
from UnderAutomation.Staubli.Soap.Data import ReversingResult as reversing_result

class IReverseKinematics:
	'''Represents the result of a reverse (inverse) kinematics computation.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_reverse_kinematics()
		else:
			self._instance = _internal

	@property
	def joint(self) -> typing.List[float]:
		'''Joint angles resulting from the reverse kinematics computation.'''
		return self._instance.Joint

	@property
	def result(self) -> ReversingResult:
		'''Result code indicating the outcome of the reverse kinematics computation.'''
		return ReversingResult(int(self._instance.Result))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IReverseKinematics):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
