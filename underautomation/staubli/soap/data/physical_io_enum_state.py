import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIoEnumState as physical_io_enum_state

class PhysicalIoEnumState(int):
	Defined = physical_io_enum_state.Defined
	Undefined = physical_io_enum_state.Undefined
	InvalidName = physical_io_enum_state.InvalidName
