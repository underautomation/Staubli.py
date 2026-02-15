from enum import IntEnum

class PowerReturnCode(IntEnum):
	'''Return code for robot power commands.'''
	Success = 0 # Success, no error occurred.
	RobotNotStopped = 1 # Cannot change power while the robot is not stopped.
	EnableTimeout = 2 # Timeout while enabling power.
	DisableTimeout = 3 # Timeout while disabling power.
	OnlyInRemoteMode = 4 # Power can only be changed in remote mode.
