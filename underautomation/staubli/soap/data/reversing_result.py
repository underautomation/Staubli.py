import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ReversingResult as reversing_result

class ReversingResult(int):
	Success = int(reversing_result.Success)
	NoConvergence = int(reversing_result.NoConvergence)
	JointOutOfRange = int(reversing_result.JointOutOfRange)
	OutOfWorkspace = int(reversing_result.OutOfWorkspace)
	InvalidConfiguration = int(reversing_result.InvalidConfiguration)
	InvalidOrientation = int(reversing_result.InvalidOrientation)
	UnsupportedKinematics = int(reversing_result.UnsupportedKinematics)
	UnconstrainedFrame = int(reversing_result.UnconstrainedFrame)
	InvalidErrorCode = int(reversing_result.InvalidErrorCode)

	def __repr__(self):
		for name, value in vars(ReversingResult).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
