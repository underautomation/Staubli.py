import typing
from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.soap.internal.soap_client_internal import SoapClientInternal
from underautomation.staubli.license.license_info import LicenseInfo
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__),  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli import StaubliController as staubli_controller

class StaubliController:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = staubli_controller()
		else:
			self._instance = _internal
	def connect(self, parameters: ConnectionParameters) -> None:
		self._instance.Connect(parameters._instance if parameters else None)
	def disconnect(self) -> None:
		self._instance.Disconnect()
	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		return LicenseInfo(None, None, staubli_controller.RegisterLicense(licensee, key))
	@property
	def address(self) -> str:
		return self._instance.Address
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
	@property
	def soap(self) -> SoapClientInternal:
		return SoapClientInternal(self._instance.Soap)
	@property
	def license_info(self) -> LicenseInfo:
		return LicenseInfo(None, None, self._instance.LicenseInfo)
