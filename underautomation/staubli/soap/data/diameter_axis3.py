from enum import IntEnum

class DiameterAxis3(IntEnum):
	'''Diameter of the third axis of the robot.'''
	Invalid = 0 # Invalid or unknown diameter.
	D20 = 1 # 20 mm diameter.
	D25 = 2 # 25 mm diameter.
