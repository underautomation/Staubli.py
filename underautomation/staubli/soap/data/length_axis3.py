import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import LengthAxis3 as length_axis3

class LengthAxis3(int):
	Invalid = int(length_axis3.Invalid)
	L100 = int(length_axis3.L100)
	L200 = int(length_axis3.L200)
	L400 = int(length_axis3.L400)
	L600 = int(length_axis3.L600)

	def __repr__(self):
		for name, value in vars(LengthAxis3).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
