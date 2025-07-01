import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ReversingResult as reversing_result

class ReversingResult(int):
	Success = reversing_result.Success
	NoConvergence = reversing_result.NoConvergence
	JointOutOfRange = reversing_result.JointOutOfRange
	OutOfWorkspace = reversing_result.OutOfWorkspace
	InvalidConfiguration = reversing_result.InvalidConfiguration
	InvalidOrientation = reversing_result.InvalidOrientation
	UnsupportedKinematics = reversing_result.UnsupportedKinematics
	UnconstrainedFrame = reversing_result.UnconstrainedFrame
	InvalidErrorCode = reversing_result.InvalidErrorCode
