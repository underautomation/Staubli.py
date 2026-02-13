import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MoveType as move_type

class MoveType(int):
	Absolute = int(move_type.Absolute)
	Relative = int(move_type.Relative)

	def __repr__(self):
		for name, value in vars(MoveType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
