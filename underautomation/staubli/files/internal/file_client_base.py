from __future__ import annotations
import typing
from underautomation.staubli.files.file_item import FileItem
from underautomation.staubli.files.on_progress_delegate import OnProgressDelegate
from UnderAutomation.Staubli.Files.Internal import FileClientBase as file_client_base
from UnderAutomation.Staubli.Files import OnProgressDelegate as on_progress_delegate

class FileClientBase:
	'''Upload, download, listing and management of the files of the controller. With a real controller, the files are accessed through the FTP server of the controller. With a controller emulated by Staubli Robotics Suite, there is no FTP server: give the path of its .controller file as address. The files are accessed in the folder of this file, which has the same tree. The paths are the same in both cases (for example "/usr/usrapp/myApp/myApp.pjx"). A path that does not start with "/" is relative to the root of the controller. The VAL 3 applications are in the folder "/usr/usrapp" of the controller (USER_APP_FOLDER): one sub-folder per application, named as the application, that contains the project file (myApp.pjx) and the other files of the application.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnects the client'''
		self._instance.Disconnect()

	def get_listing(self, path: str) -> typing.List[FileItem]:
		'''Lists the files and folders of a folder of the controller

		:param path: Path of the folder on the controller (for example "/usr/usrapp")
		:returns: The files and folders of the folder
		'''
		return [FileItem(x) for x in self._instance.GetListing(path)]

	def get_file_info(self, path: str) -> FileItem:
		'''Gets information about a file or a folder of the controller

		:param path: Path of the file or folder on the controller
		:returns: The information, or null when the file or folder does not exist
		'''
		return FileItem(self._instance.GetFileInfo(path))

	def file_exists(self, path: str) -> bool:
		'''Checks if a file exists on the controller

		:param path: Path of the file on the controller
		:returns: True if the file exists
		'''
		return self._instance.FileExists(path)

	def directory_exists(self, path: str) -> bool:
		'''Checks if a folder exists on the controller

		:param path: Path of the folder on the controller
		:returns: True if the folder exists
		'''
		return self._instance.DirectoryExists(path)

	def create_directory(self, path: str) -> None:
		'''Creates a folder on the controller, with its parent folders when they do not exist. Nothing is done when the folder exists.

		:param path: Path of the new folder on the controller
		'''
		self._instance.CreateDirectory(path)

	def delete_file(self, path: str) -> None:
		'''Deletes a file of the controller

		:param path: Path of the file on the controller
		'''
		self._instance.DeleteFile(path)

	def delete_directory(self, path: str) -> None:
		'''Deletes a folder of the controller and all its content

		:param path: Path of the folder on the controller
		'''
		self._instance.DeleteDirectory(path)

	def rename(self, path: str, newPath: str) -> None:
		'''Renames or moves a file or a folder of the controller

		:param path: Path of the file or folder on the controller
		:param newPath: New path of the file or folder on the controller
		'''
		self._instance.Rename(path, newPath)

	def upload_file_to_controller(self, localPath: str, remotePath: str, createRemoteDir: bool=False, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Uploads a local file to the controller. The file of the controller is replaced when it exists.

		:param localPath: Path of the file on this computer
		:param remotePath: Path of the file on the controller (for example "/usr/usrapp/myApp/myApp.pjx")
		:param createRemoteDir: Create the folder of the file on the controller when it does not exist
		:param progress: Called during the transfer with the percentage of the file transferred
		'''
		self._instance.UploadFileToController(localPath, remotePath, createRemoteDir, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def upload_bytes_to_controller(self, data: typing.List[int], remotePath: str, createRemoteDir: bool=False, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Uploads data as a file to the controller. The file of the controller is replaced when it exists.

		:param data: Content of the file
		:param remotePath: Path of the file on the controller (for example "/usr/usrapp/myApp/myApp.pjx")
		:param createRemoteDir: Create the folder of the file on the controller when it does not exist
		:param progress: Called during the transfer with the percentage of the file transferred
		'''
		self._instance.UploadBytesToController(data, remotePath, createRemoteDir, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def upload_application_to_controller(self, localAppFolder: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> str:
		'''Uploads a complete VAL 3 application to the controller. The local folder of the application, named as the application and with its project file inside (for example C:\\MyApps\\myApp\\myApp.pjx), is copied with its sub-folders to "/usr/usrapp/myApp" (USER_APP_FOLDER). When the application already exists on the controller, its folder is deleted first: the files that are not in the local folder are removed. Stop and unload the application before (robot.Soap.StopAndUnloadAll()), then load it after (robot.Soap.LoadProject("Disk://myApp/myApp.pjx")).

		:param localAppFolder: Folder of the application on this computer
		:param progress: Called during the transfer with the percentage of all the files transferred
		:returns: Path of the folder of the application on the controller (for example "/usr/usrapp/myApp")
		'''
		return self._instance.UploadApplicationToController(localAppFolder, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def download_file_from_controller(self, localPath: str, remotePath: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> None:
		'''Downloads a file of the controller to a local file. The local file is replaced when it exists, and its folder is created when it does not exist.

		:param localPath: Path of the file on this computer
		:param remotePath: Path of the file on the controller (for example "/usr/usrapp/myApp/myApp.pjx")
		:param progress: Called during the transfer with the percentage of the file transferred
		'''
		self._instance.DownloadFileFromController(localPath, remotePath, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	def download_bytes_from_controller(self, remotePath: str, progress: typing.Callable[[float], None] | OnProgressDelegate=None) -> typing.List[int]:
		'''Downloads a file of the controller and returns its content

		:param remotePath: Path of the file on the controller (for example "/usr/usrapp/myApp/myApp.pjx")
		:param progress: Called during the transfer with the percentage of the file transferred
		:returns: The content of the file
		'''
		return self._instance.DownloadBytesFromController(remotePath, (progress._instance if isinstance(progress, OnProgressDelegate) else on_progress_delegate(lambda _x0: progress(_x0))) if progress else None)

	@property
	def ip(self) -> str:
		'''IP or host name of the controller. Null with an emulated controller.'''
		return self._instance.Ip

	@property
	def port(self) -> int:
		'''Port of the FTP server of the controller. 0 with an emulated controller.'''
		return self._instance.Port

	@property
	def controller_file(self) -> str:
		'''Full path of the .controller file of the controller emulated by Staubli Robotics Suite. Null with a real controller.'''
		return self._instance.ControllerFile

	@property
	def controller_folder(self) -> str:
		'''Full path of the folder of the .controller file: root of the files of the emulated controller. Null with a real controller.'''
		return self._instance.ControllerFolder

	@property
	def is_simulated(self) -> bool:
		'''True when the files are accessed in the folder of the .controller file of a controller emulated by Staubli Robotics Suite, false when they are accessed through FTP'''
		return self._instance.IsSimulated

	@property
	def enabled(self) -> bool:
		'''True when the client is connected'''
		return self._instance.Enabled

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Folder of the VAL 3 applications on the controller. Each application is in a sub-folder named as the application (for example "/usr/usrapp/myApp/myApp.pjx"). The project path "Disk://myApp/myApp.pjx" of robot.Soap.LoadProject(...) is this file.
FileClientBase.USER_APP_FOLDER = file_client_base.USER_APP_FOLDER
