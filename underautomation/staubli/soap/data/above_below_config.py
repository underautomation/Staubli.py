from enum import IntEnum

class AboveBelowConfig(IntEnum):
	'''Configuration for above/below joint orientation.'''
	Same = 0 # Keep the same configuration as the current one.
	Above = 1 # Above configuration.
	Below = 2 # Below configuration.
	Free = 3 # Free configuration (no constraint).
