import typing
from underautomation.staubli.soap.data.dh_parameters import DhParameters
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetRobotDhParametersResponse as get_robot_dh_parameters_response

class GetRobotDhParametersResponse:
	def __init__(self, dhParametersArray: typing.List[DhParameters], lastDParam: float, _internal = 0):
		if(_internal == 0):
			self._instance = get_robot_dh_parameters_response(dhParametersArray, lastDParam)
		else:
			self._instance = _internal
	@property
	def dh_parameters_array(self) -> typing.List[DhParameters]:
		return [DhParameters(x) for x in self._instance.dhParametersArray]
	@dh_parameters_array.setter
	def dh_parameters_array(self, value: typing.List[DhParameters]):
		self._instance.dhParametersArray = value._instance if value else None
	@property
	def last_d_param(self) -> float:
		return self._instance.lastDParam
	@last_d_param.setter
	def last_d_param(self, value: float):
		self._instance.lastDParam = value
