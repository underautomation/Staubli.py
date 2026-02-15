import typing
from underautomation.staubli.soap.data.dh_parameters import DhParameters
from UnderAutomation.Staubli.Soap.Internal.V2 import GetRobotDhParametersResponse as get_robot_dh_parameters_response

class GetRobotDhParametersResponse:
	'''SOAP response containing the robot's Denavit-Hartenberg parameters.'''
	def __init__(self, dhParametersArray: typing.List[DhParameters], lastDParam: float, _internal = 0):
		'''Initializes a new instance with the specified DH parameters.

		:param dhParametersArray: Array of DH parameters per joint.
		:param lastDParam: Last D parameter value.
		'''
		if(_internal == 0):
			self._instance = get_robot_dh_parameters_response(dhParametersArray, lastDParam)
		else:
			self._instance = _internal

	@property
	def dh_parameters_array(self) -> typing.List[DhParameters]:
		'''Array of Denavit-Hartenberg parameters for each joint.'''
		return [DhParameters(x) for x in self._instance.dhParametersArray]

	@dh_parameters_array.setter
	def dh_parameters_array(self, value: typing.List[DhParameters]):
		self._instance.dhParametersArray = value._instance if value else None

	@property
	def last_d_param(self) -> float:
		'''Last D parameter value.'''
		return self._instance.lastDParam

	@last_d_param.setter
	def last_d_param(self, value: float):
		self._instance.lastDParam = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetRobotDhParametersResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
