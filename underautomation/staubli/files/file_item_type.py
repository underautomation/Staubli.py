from enum import IntEnum

class FileItemType(IntEnum):
	'''Type of an item of the controller file system'''
	File = 0 # A file
	Directory = 1 # A folder
