from __future__ import annotations
import typing
from underautomation.staubli.files.file_item_type import FileItemType
from datetime import datetime, timedelta
from UnderAutomation.Staubli.Files import FileItem as file_item
from UnderAutomation.Staubli.Files import FileItemType as file_item_type

class FileItem:
	'''A file or a folder of the controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the file or folder, without its path (for example "myApp.pjx")'''
		return self._instance.Name

	@property
	def full_name(self) -> str:
		'''Full path of the file or folder on the controller (for example "/usr/usrapp/myApp/myApp.pjx")'''
		return self._instance.FullName

	@property
	def type(self) -> FileItemType:
		'''File or folder'''
		return FileItemType(int(self._instance.Type))

	@property
	def size(self) -> int:
		'''Size of the file in bytes. 0 for a folder, and 0 when the controller does not give the size.'''
		return self._instance.Size

	@property
	def modified(self) -> datetime:
		'''Date and time of the last modification, as given by the controller. With a controller emulated by Staubli Robotics Suite, local time of the computer.'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.Modified.Ticks // 10)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
