import typing
from underautomation.staubli.soap.data.val_application import ValApplication
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V1 import GetApplications1Response as get_applications1_response

class GetApplications1Response:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_applications1_response()
		else:
			self._instance = _internal
	@property
	def applications(self) -> typing.List[ValApplication]:
		return [ValApplication(x) for x in self._instance.Applications]
	@applications.setter
	def applications(self, value: typing.List[ValApplication]):
		self._instance.Applications = value
