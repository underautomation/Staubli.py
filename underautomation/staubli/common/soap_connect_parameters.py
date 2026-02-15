import typing
from underautomation.staubli.soap.internal.soap_connect_parameters_base import SoapConnectParametersBase
from UnderAutomation.Staubli.Common import SoapConnectParameters as soap_connect_parameters

class SoapConnectParameters(SoapConnectParametersBase):
	'''SOAP connection parameters for communicating with the Staubli robot controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should use this service (default: true)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SoapConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default port for SOAP service
SoapConnectParameters.DEFAULT_PORT = soap_connect_parameters.DEFAULT_PORT
