import typing
from UnderAutomation.Staubli.Soap.Internal.V3 import StopMotionRequest as stop_motion_request

class StopMotionRequest:
	'''SOAP request to stop the robot motion.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the StopMotionRequest class.'''
		if(_internal == 0):
			self._instance = stop_motion_request()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StopMotionRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
