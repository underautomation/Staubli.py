import typing
from underautomation.staubli.soap.data.joint_range import JointRange
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V1 import GetJointRangeResponse as get_joint_range_response

class GetJointRangeResponse:
	def __init__(self, range: JointRange, _internal = 0):
		if(_internal == 0):
			self._instance = get_joint_range_response(range)
		else:
			self._instance = _internal
	@property
	def range(self) -> JointRange:
		return JointRange(self._instance.range)
	@range.setter
	def range(self, value: JointRange):
		self._instance.range = value
