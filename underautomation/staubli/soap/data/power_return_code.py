import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PowerReturnCode as power_return_code

class PowerReturnCode(int):
	Success = power_return_code.Success
	RobotNotStopped = power_return_code.RobotNotStopped
	EnableTimeout = power_return_code.EnableTimeout
	DisableTimeout = power_return_code.DisableTimeout
	OnlyInRemoteMode = power_return_code.OnlyInRemoteMode
