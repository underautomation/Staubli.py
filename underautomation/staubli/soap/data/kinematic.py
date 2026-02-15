from enum import IntEnum

class Kinematic(IntEnum):
	'''Robot kinematic type.'''
	Invalid = 0 # Invalid or unknown kinematic type.
	Anthropomorph6 = 1 # 6-axis anthropomorphic robot.
	Anthrioparallel6 = 2 # 6-axis anthropomorphic parallel robot.
	Anthropomorph5 = 3 # 5-axis anthropomorphic robot.
	Scara = 4 # SCARA robot.
	Eisenmann = 5 # Eisenmann kinematic type.
