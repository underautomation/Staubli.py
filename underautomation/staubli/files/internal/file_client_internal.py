from __future__ import annotations
import typing
from underautomation.staubli.files.internal.file_client_base import FileClientBase
from UnderAutomation.Staubli.Files.Internal import FileClientInternal as file_client_internal

class FileClientInternal(FileClientBase):
	'''File client of StaubliController, connected by connect()'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
