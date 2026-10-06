from __future__ import annotations
import typing
from UnderAutomation.Staubli.Files.Internal import FileConnectParametersBase as file_connect_parameters_base

class FileConnectParametersBase:
	'''Base class for the connection parameters of the file client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def user(self) -> str:
		'''User of the FTP server of the controller (default: default). Not used with a controller emulated by Staubli Robotics Suite.'''
		return self._instance.User

	@user.setter
	def user(self, value: str):
		self._instance.User = value

	@property
	def password(self) -> str:
		'''Password of the user (default: default). Not used with a controller emulated by Staubli Robotics Suite.'''
		return self._instance.Password

	@password.setter
	def password(self, value: str):
		self._instance.Password = value

	@property
	def port(self) -> int:
		'''Port of the FTP server of the controller (default: 21)'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def timeout_ms(self) -> int:
		'''Timeout of the FTP connection and of the transfers, in milliseconds (default: 30000)'''
		return self._instance.TimeoutMs

	@timeout_ms.setter
	def timeout_ms(self, value: int):
		self._instance.TimeoutMs = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
