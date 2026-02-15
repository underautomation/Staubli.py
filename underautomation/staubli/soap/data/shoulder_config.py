from enum import IntEnum

class ShoulderConfig(IntEnum):
	'''Shoulder configuration for the robot arm.'''
	Same = 0 # Keep the same configuration as the current one.
	Lefty = 1 # Left-handed configuration.
	Righty = 2 # Right-handed configuration.
	Free = 3 # Free configuration (no constraint).
