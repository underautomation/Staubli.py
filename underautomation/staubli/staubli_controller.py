from __future__ import annotations
import typing
from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.soap.internal.soap_client_internal import SoapClientInternal
from underautomation.staubli.files.internal.file_client_internal import FileClientInternal
from underautomation.staubli.license.license_info import LicenseInfo
from UnderAutomation.Staubli import StaubliController as staubli_controller

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class StaubliController:
	'''Main class of the SDK that represents a connection to a Staubli robot controller'''
	def __init__(self, _internal = 0):
		'''Instanciate a new Staubli robot controller connection'''
		if(_internal == 0):
			self._instance = staubli_controller()
		else:
			self._instance = _internal

	def connect(self, ip_or_parameters: str | ConnectionParameters) -> None:
		'''Connect to robot by IP with default connection parameters
		Initialize a conenction to the robot with specified parameters
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

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
		'''IP or robot name, or path of the .controller file of a controller emulated by Staubli Robotics Suite'''
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
	def file(self) -> FileClientInternal:
		'''File client: upload, download, listing and management of the files of the controller. Uses the FTP server of a real controller, or the folder of the .controller file of a controller emulated by Staubli Robotics Suite. The VAL 3 applications are in the folder "/usr/usrapp": robot.File.UploadApplicationToController(...) sends a complete application.'''
		return FileClientInternal(self._instance.File)

	@staticmethod
	def _get_license_info() -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, staubli_controller.LicenseInfo)

	license_info = _StaticProperty(_get_license_info)
	del _get_license_info

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
