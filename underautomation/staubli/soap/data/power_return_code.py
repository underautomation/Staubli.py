import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PowerReturnCode as power_return_code

class PowerReturnCode(int):
	Success = int(power_return_code.Success)
	RobotNotStopped = int(power_return_code.RobotNotStopped)
	EnableTimeout = int(power_return_code.EnableTimeout)
	DisableTimeout = int(power_return_code.DisableTimeout)
	OnlyInRemoteMode = int(power_return_code.OnlyInRemoteMode)

	def __repr__(self):
		for name, value in vars(PowerReturnCode).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
