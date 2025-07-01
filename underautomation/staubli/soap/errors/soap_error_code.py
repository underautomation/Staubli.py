import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Errors import SoapErrorCode as soap_error_code

class SoapErrorCode(int):
	Unknown = soap_error_code.Unknown
	InvalidCredentials = soap_error_code.InvalidCredentials
	TaskNotFound = soap_error_code.TaskNotFound
	MismatchedCode = soap_error_code.MismatchedCode
	ProgramNotFound = soap_error_code.ProgramNotFound
	TaskAlreadyLocked = soap_error_code.TaskAlreadyLocked
	SinReturnCodeNok = soap_error_code.SinReturnCodeNok
	SchedulingModeError = soap_error_code.SchedulingModeError
	ApplicationNotFound = soap_error_code.ApplicationNotFound
	StackFrameNotFound = soap_error_code.StackFrameNotFound
	ProgramLineNotFound = soap_error_code.ProgramLineNotFound
	ReadAccessErrorCode = soap_error_code.ReadAccessErrorCode
	SetPosNotSimulCode = soap_error_code.SetPosNotSimulCode
	InvalidSessionIdCode = soap_error_code.InvalidSessionIdCode
	WriteAccessErrorCode = soap_error_code.WriteAccessErrorCode
	CannotStartApplication = soap_error_code.CannotStartApplication
	ClientAlreadyConnected = soap_error_code.ClientAlreadyConnected
	IoWriteAccessErrorCode = soap_error_code.IoWriteAccessErrorCode
	ClientCommunicationError = soap_error_code.ClientCommunicationError
	IoWriteAccessErrorValidation = soap_error_code.IoWriteAccessErrorValidation
	IoWriteAccessErrorWorkingMode = soap_error_code.IoWriteAccessErrorWorkingMode
	InvalidRobotIdCode = soap_error_code.InvalidRobotIdCode
