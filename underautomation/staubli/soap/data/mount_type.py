from enum import IntEnum

class MountType(IntEnum):
	'''Robot mounting type.'''
	Invalid = 0 # Invalid or unknown mount type.
	Floor = 1 # Robot is floor-mounted.
	Ceiling = 2 # Robot is ceiling-mounted.
	Wall = 3 # Robot is wall-mounted.
