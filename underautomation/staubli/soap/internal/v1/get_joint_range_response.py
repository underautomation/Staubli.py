import typing
from underautomation.staubli.soap.data.joint_range import JointRange
from UnderAutomation.Staubli.Soap.Internal.V1 import GetJointRangeResponse as get_joint_range_response

class GetJointRangeResponse:
	'''SOAP response containing a robot's joint range limits.'''
	def __init__(self, range: JointRange, _internal = 0):
		'''Initializes a new instance with the specified joint range.

		:param range: Joint range data.
		'''
		if(_internal == 0):
			self._instance = get_joint_range_response(range)
		else:
			self._instance = _internal

	@property
	def range(self) -> JointRange:
		'''Joint range limits for each axis.'''
		return JointRange(self._instance.range)

	@range.setter
	def range(self, value: JointRange):
		self._instance.range = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetJointRangeResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
