from enum import IntEnum

class ReversingResult(IntEnum):
	'''Result code for reverse kinematics computation.'''
	Success = 0 # Reverse kinematics succeeded.
	NoConvergence = 1 # The algorithm did not converge to a solution.
	JointOutOfRange = 2 # The computed joint position is out of range.
	OutOfWorkspace = 3 # The target is outside the robot workspace.
	InvalidConfiguration = 4 # The specified configuration is invalid.
	InvalidOrientation = 5 # The specified orientation is invalid.
	UnsupportedKinematics = 6 # The robot kinematics type is not supported.
	UnconstrainedFrame = 7 # The frame is unconstrained.
	InvalidErrorCode = 8 # Invalid error code returned.
