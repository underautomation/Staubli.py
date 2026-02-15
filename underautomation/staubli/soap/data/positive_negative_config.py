from enum import IntEnum

class PositiveNegativeConfig(IntEnum):
	'''Positive/negative configuration for a robot joint.'''
	Same = 0 # Keep the same configuration as the current one.
	Positive = 1 # Positive configuration.
	Negative = 2 # Negative configuration.
	Free = 3 # Free configuration (no constraint).
