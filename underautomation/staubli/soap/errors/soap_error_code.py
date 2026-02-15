from enum import IntEnum

class SoapErrorCode(IntEnum):
	'''Error codes returned by the SOAP service.'''
	Unknown = -1 # Unknown or unrecognized error code.
	InvalidCredentials = 0 # The provided credentials are invalid.
	TaskNotFound = 1 # The specified task was not found.
	MismatchedCode = 2 # Mismatched code error.
	ProgramNotFound = 3 # The specified program was not found.
	TaskAlreadyLocked = 4 # The task is already locked by another client.
	SinReturnCodeNok = 5 # SIN return code indicates failure.
	SchedulingModeError = 6 # Scheduling mode error.
	ApplicationNotFound = 7 # The specified application was not found.
	StackFrameNotFound = 8 # The specified stack frame was not found.
	ProgramLineNotFound = 9 # The specified program line was not found.
	ReadAccessErrorCode = 10 # Read access error.
	SetPosNotSimulCode = 11 # Cannot set position outside simulation mode.
	InvalidSessionIdCode = 12 # The session ID is invalid or expired.
	WriteAccessErrorCode = 13 # Write access error.
	CannotStartApplication = 14 # Cannot start the application.
	ClientAlreadyConnected = 15 # A client is already connected.
	IoWriteAccessErrorCode = 16 # I/O write access error.
	ClientCommunicationError = 17 # Client communication error.
	IoWriteAccessErrorValidation = 18 # I/O write access validation error.
	IoWriteAccessErrorWorkingMode = 19 # I/O write access error due to working mode.
	InvalidRobotIdCode = 20 # The specified robot ID is invalid.
