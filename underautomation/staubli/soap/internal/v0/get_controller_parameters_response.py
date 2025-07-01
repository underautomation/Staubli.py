import typing
from underautomation.staubli.soap.data.parameter import Parameter
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V0 import GetControllerParametersResponse as get_controller_parameters_response

class GetControllerParametersResponse:
	def __init__(self, out: typing.List[Parameter], _internal = 0):
		if(_internal == 0):
			self._instance = get_controller_parameters_response(out)
		else:
			self._instance = _internal
	@property
	def out(self) -> typing.List[Parameter]:
		return [Parameter(x) for x in self._instance.out]
	@out.setter
	def out(self, value: typing.List[Parameter]):
		self._instance.out = value
