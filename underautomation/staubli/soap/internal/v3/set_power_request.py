import typing
from UnderAutomation.Staubli.Soap.Internal.V3 import SetPowerRequest as set_power_request

class SetPowerRequest:
	'''SOAP request to set the robot power state.'''
	def __init__(self, power: bool, _internal = 0):
		'''Initializes a new instance with the specified power state.

		:param power: True to power on, false to power off.
		'''
		if(_internal == 0):
			self._instance = set_power_request(power)
		else:
			self._instance = _internal

	@property
	def power(self) -> bool:
		'''Desired power state. True to power on, false to power off.'''
		return self._instance.power

	@power.setter
	def power(self, value: bool):
		self._instance.power = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetPowerRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
