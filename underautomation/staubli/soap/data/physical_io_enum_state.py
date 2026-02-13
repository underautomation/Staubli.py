import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIoEnumState as physical_io_enum_state

class PhysicalIoEnumState(int):
	Defined = int(physical_io_enum_state.Defined)
	Undefined = int(physical_io_enum_state.Undefined)
	InvalidName = int(physical_io_enum_state.InvalidName)

	def __repr__(self):
		for name, value in vars(PhysicalIoEnumState).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
