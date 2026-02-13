import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code

class MotionReturnCode(int):
	Success = int(motion_return_code.Success)
	NotReady = int(motion_return_code.NotReady)
	ParameterError = int(motion_return_code.ParameterError)
	MisuseError = int(motion_return_code.MisuseError)
	UnexpectedError = int(motion_return_code.UnexpectedError)

	def __repr__(self):
		for name, value in vars(MotionReturnCode).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
