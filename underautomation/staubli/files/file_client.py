from __future__ import annotations
import typing
from underautomation.staubli.files.internal.file_client_base import FileClientBase
from UnderAutomation.Staubli.Files import FileClient as file_client

class FileClient(FileClientBase):
	'''Standalone client for the files of a Staubli controller: upload, download, listing and management. With a real controller, the files are accessed through the FTP server of the controller. With a controller emulated by Staubli Robotics Suite, they are accessed in the folder of its .controller file.'''
	def __init__(self, _internal = 0):
		'''Create a new instance of FileClient'''
		if(_internal == 0):
			self._instance = file_client()
		else:
			self._instance = _internal

	def connect(self, address: str, user: str, password: str, port: int=21, timeoutMs: int=30000) -> None:
		'''Connect to a controller

		:param address: IP or host name of a real controller. For a controller emulated by Staubli Robotics Suite, path of its .controller file (local path, or UNC path when the emulation runs on another computer).
		:param user: User of the FTP server of the controller. Not used with an emulated controller.
		:param password: Password of the user. Not used with an emulated controller.
		:param port: Port of the FTP server of the controller
		:param timeoutMs: Timeout of the FTP connection and of the transfers, in milliseconds
		'''
		self._instance.Connect(address, user, password, port, timeoutMs)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
