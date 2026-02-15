from enum import IntEnum

class BlendType(IntEnum):
	'''Blend mode used during motion transitions between segments.'''
	BlendOff = 0 # No blending; the robot stops at each target point.
	BlendJoint = 1 # Joint-space blending between motion segments.
	BlendCartesian = 2 # Cartesian-space blending between motion segments.
