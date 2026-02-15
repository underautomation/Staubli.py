from enum import IntEnum

class LengthAxis3(IntEnum):
	'''Length of the third axis of the robot.'''
	Invalid = 0 # Invalid or unknown length.
	L100 = 1 # 100 mm length.
	L200 = 2 # 200 mm length.
	L400 = 3 # 400 mm length.
	L600 = 4 # 600 mm length.
