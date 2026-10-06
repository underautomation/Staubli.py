from __future__ import annotations
import typing
from UnderAutomation.Staubli.Files import FileException as file_exception

class FileException:
	'''Exception thrown when an operation on the files of the controller fails: the controller refused it, the file does not exist, or the communication failed. The message gives the reason and, when it is known, what to do.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_exception()
		else:
			self._instance = _internal

	@property
	def remote_path(self) -> str:
		'''Path of the file or folder on the controller concerned by the operation. Null when the operation has no path.'''
		return self._instance.RemotePath

	@property
	def reply_code(self) -> int:
		'''FTP reply code returned by the controller (for example 550). 0 when the controller did not reply, and with an emulated controller.'''
		return self._instance.ReplyCode

	@property
	def reply_message(self) -> str:
		'''Reply text returned by the controller. Null when the controller did not reply, and with an emulated controller.'''
		return self._instance.ReplyMessage

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
