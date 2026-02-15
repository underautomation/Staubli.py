from enum import IntEnum

class StartApplicationError(IntEnum):
	'''Error codes that can occur when starting an application on the controller.'''
	MemoryFull = 0 # Not enough memory to start the application.
	LibraryBusy = 1 # The library is currently busy.
	LibraryInvalidZip = 2 # The library ZIP file is invalid.
	DataNotFound = 3 # The required data was not found.
	DataBusy = 4 # The data is currently busy.
	DataInvalidName = 5 # The data name is invalid.
	DataAlreadyExists = 6 # The data already exists.
	DataInvalidSize = 7 # The data size is invalid.
	DataNotAnArray = 8 # The data is not an array.
	RoutineInvalidName = 9 # The routine name is invalid.
	RoutineAlreadyExists = 10 # The routine already exists.
	RoutineNameTooLong = 11 # The routine name is too long.
	RoutineInvalidParamPosition = 12 # The routine parameter position is invalid.
	RoutineNotFound = 13 # The routine was not found.
	RoutineBusy = 14 # The routine is currently busy.
	ProjectBusy = 15 # The project is currently busy.
	ProjectInvalidName = 16 # The project name is invalid.
	ProjectInvalidAlias = 17 # The project alias is invalid.
	ProjectAliasAlreadyUsed = 18 # The project alias is already in use.
	ProjectAlreadyExists = 19 # The project already exists.
	ProjectCodeError = 20 # A code error occurred in the project.
	ProjectDataError = 21 # A data error occurred in the project.
	StartRoutineNotFound = 22 # The start routine was not found.
	ProjectInvalidMain = 23 # The project main entry point is invalid.
	ProjectInvalidProject = 24 # The project is invalid.
	StopRoutineNotFound = 25 # The stop routine was not found.
	ProjectInvalidDestructor = 26 # The project destructor is invalid.
	ProjectDefaultStackTooSmall = 27 # The default stack size is too small.
	ProjectAlreadyRunning = 28 # The project is already running.
	ProjectAlreadyEnding = 29 # The project is already ending.
	ProjectLocked = 30 # The project is locked.
	ProjectFileError = 31 # A file error occurred in the project.
	ProjectFilemanagerNotFound = 32 # The file manager was not found.
	ProjectLibraryError = 33 # A library error occurred in the project.
	ProjectUnresolvedSymbol = 34 # An unresolved symbol was found in the project.
	ProjectInconsistantResolvedSymbol = 35 # An inconsistent resolved symbol was found.
	ProjectInterfaceStillUsed = 36 # An interface is still in use.
	ProjectUsedAsStruct = 37 # The project is used as a struct.
	ProjectInterfaceTaskNotKilled = 38 # An interface task has not been killed.
	ProjectInvalidTypename = 39 # The type name is invalid.
	ProjectTypenameAlreadyUsed = 40 # The type name is already in use.
	ProjectTypeProjectError = 41 # A type project error occurred.
	ProjectTypeBusy = 42 # The type is currently busy.
	ProjectCircularReference = 43 # A circular reference was detected in the project.
