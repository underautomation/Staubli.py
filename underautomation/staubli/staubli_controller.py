import typing
from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.soap.internal.soap_client_internal import SoapClientInternal
from underautomation.staubli.license.license_info import LicenseInfo
from UnderAutomation.Staubli import StaubliController as staubli_controller

class StaubliController:
	'''Main class of the SDK that represents a connection to a Staubli robot controller'''
	def __init__(self, _internal = 0):
		'''Instanciate a new Staubli robot controller connection'''
		if(_internal == 0):
			self._instance = staubli_controller()
		else:
			self._instance = _internal

	def connect(self, parameters: ConnectionParameters) -> None:
		'''Initialize a conenction to the robot with specified parameters'''
		self._instance.Connect(parameters._instance if parameters else None)

	def disconnect(self) -> None:
		'''Disconnect all services connected to the robot'''
		self._instance.Disconnect()

	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		'''If you have a license And a key, please call this static method to register the product And exit the trial period ou can register a product even if the trial period has ended

		:param licensee: Your organization name
		:param key: The associated key supplied by UnderAutomation
		:returns: Information about the supplied license
		'''
		return LicenseInfo(None, None, staubli_controller.RegisterLicense(licensee, key))

	@property
	def address(self) -> str:
		'''IP or robot name'''
		return self._instance.Address

	@property
	def enabled(self) -> bool:
		'''Check if the robot is connected'''
		return self._instance.Enabled

	@property
	def soap(self) -> SoapClientInternal:
		'''Internal SOAP client used to communicate with the robot controller.'''
		return SoapClientInternal(self._instance.Soap)

	@property
	def license_info(self) -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, StaubliController):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
