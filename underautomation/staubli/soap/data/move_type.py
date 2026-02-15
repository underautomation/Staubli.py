from enum import IntEnum

class MoveType(IntEnum):
	'''Specifies whether the motion is absolute or relative.'''
	Absolute = 0 # Absolute motion in the reference frame.
	Relative = 1 # Relative motion from the current position.
