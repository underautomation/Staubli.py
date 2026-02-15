from enum import IntEnum

class PhysicalIoEnumState(IntEnum):
	'''Definition state of a physical I/O.'''
	Defined = 0 # The I/O is defined and available.
	Undefined = 1 # The I/O is not defined.
	InvalidName = 2 # The I/O name is invalid.
