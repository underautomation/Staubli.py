import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Errors import SoapErrorCode as soap_error_code

class SoapErrorCode(int):
	Unknown = int(soap_error_code.Unknown)
	InvalidCredentials = int(soap_error_code.InvalidCredentials)
	TaskNotFound = int(soap_error_code.TaskNotFound)
	MismatchedCode = int(soap_error_code.MismatchedCode)
	ProgramNotFound = int(soap_error_code.ProgramNotFound)
	TaskAlreadyLocked = int(soap_error_code.TaskAlreadyLocked)
	SinReturnCodeNok = int(soap_error_code.SinReturnCodeNok)
	SchedulingModeError = int(soap_error_code.SchedulingModeError)
	ApplicationNotFound = int(soap_error_code.ApplicationNotFound)
	StackFrameNotFound = int(soap_error_code.StackFrameNotFound)
	ProgramLineNotFound = int(soap_error_code.ProgramLineNotFound)
	ReadAccessErrorCode = int(soap_error_code.ReadAccessErrorCode)
	SetPosNotSimulCode = int(soap_error_code.SetPosNotSimulCode)
	InvalidSessionIdCode = int(soap_error_code.InvalidSessionIdCode)
	WriteAccessErrorCode = int(soap_error_code.WriteAccessErrorCode)
	CannotStartApplication = int(soap_error_code.CannotStartApplication)
	ClientAlreadyConnected = int(soap_error_code.ClientAlreadyConnected)
	IoWriteAccessErrorCode = int(soap_error_code.IoWriteAccessErrorCode)
	ClientCommunicationError = int(soap_error_code.ClientCommunicationError)
	IoWriteAccessErrorValidation = int(soap_error_code.IoWriteAccessErrorValidation)
	IoWriteAccessErrorWorkingMode = int(soap_error_code.IoWriteAccessErrorWorkingMode)
	InvalidRobotIdCode = int(soap_error_code.InvalidRobotIdCode)

	def __repr__(self):
		for name, value in vars(SoapErrorCode).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
