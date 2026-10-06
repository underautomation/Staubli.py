from __future__ import annotations
import typing
from underautomation.staubli.files.internal.file_connect_parameters_base import FileConnectParametersBase
from UnderAutomation.Staubli.Common import FileConnectParameters as file_connect_parameters

class FileConnectParameters(FileConnectParametersBase):
	'''Connection parameters of the file client (robot.File). With a real controller, the files are accessed through the FTP server of the controller, with the user and the password of these parameters. With a controller emulated by Staubli Robotics Suite, give the path of its .controller file as address: the files are accessed in the folder of this file.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Should use this service (default: false)'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default port of the FTP server
FileConnectParameters.DEFAULT_PORT = file_connect_parameters.DEFAULT_PORT

# Default timeout of the FTP connection and of the transfers, in milliseconds
FileConnectParameters.DEFAULT_TIMEOUT_MS = file_connect_parameters.DEFAULT_TIMEOUT_MS
