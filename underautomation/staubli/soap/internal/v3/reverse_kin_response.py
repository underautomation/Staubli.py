import typing
from underautomation.staubli.soap.data.i_reverse_kinematics import IReverseKinematics
from underautomation.staubli.soap.data.reversing_result import ReversingResult
from UnderAutomation.Staubli.Soap.Internal.V3 import ReverseKinResponse as reverse_kin_response
from UnderAutomation.Staubli.Soap.Data import ReversingResult as reversing_result

class ReverseKinResponse(IReverseKinematics):
	'''SOAP response containing the reverse kinematics result.'''
	def __init__(self, jointOut: typing.List[float], reversingResult: ReversingResult, _internal = 0):
		'''Initializes a new instance with the specified joint positions and result.

		:param jointOut: Computed joint positions in radians.
		:param reversingResult: Result code of the reverse kinematics computation.
		'''
		if(_internal == 0):
			self._instance = reverse_kin_response(jointOut, reversingResult)
		else:
			self._instance = _internal

	@property
	def joint(self) -> typing.List[float]:
		'''Computed joint positions in radians.'''
		return self._instance.Joint

	@joint.setter
	def joint(self, value: typing.List[float]):
		self._instance.Joint = value

	@property
	def result(self) -> ReversingResult:
		'''Result code of the reverse kinematics computation.'''
		return ReversingResult(int(self._instance.Result))

	@result.setter
	def result(self, value: ReversingResult):
		self._instance.Result = reversing_result(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ReverseKinResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
