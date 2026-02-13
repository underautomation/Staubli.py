import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MountType as mount_type

class MountType(int):
	Invalid = int(mount_type.Invalid)
	Floor = int(mount_type.Floor)
	Ceiling = int(mount_type.Ceiling)
	Wall = int(mount_type.Wall)

	def __repr__(self):
		for name, value in vars(MountType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
