import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MountType as mount_type

class MountType(int):
	Invalid = mount_type.Invalid
	Floor = mount_type.Floor
	Ceiling = mount_type.Ceiling
	Wall = mount_type.Wall
