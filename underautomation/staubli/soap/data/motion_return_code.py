import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class MotionReturnCode(int):
	Success = motion_return_code.Success
	NotReady = motion_return_code.NotReady
	ParameterError = motion_return_code.ParameterError
	MisuseError = motion_return_code.MisuseError
	UnexpectedError = motion_return_code.UnexpectedError
