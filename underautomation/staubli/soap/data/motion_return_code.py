from enum import IntEnum

class MotionReturnCode(IntEnum):
	'''Return code for robot motion commands.'''
	Success = 0 # Success, no error occurred.
	NotReady = 1 # The robot is not ready to execute motion.
	ParameterError = 2 # Invalid parameter provided to the motion command.
	MisuseError = 3 # Motion command misuse error.
	UnexpectedError = 4 # An unexpected error occurred during motion.
