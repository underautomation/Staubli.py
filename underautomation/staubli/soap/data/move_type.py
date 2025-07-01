import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MoveType as move_type

class MoveType(int):
	Absolute = move_type.Absolute
	Relative = move_type.Relative
