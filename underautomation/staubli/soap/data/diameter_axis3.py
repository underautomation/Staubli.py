import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import DiameterAxis3 as diameter_axis3

class DiameterAxis3(int):
	Invalid = int(diameter_axis3.Invalid)
	D20 = int(diameter_axis3.D20)
	D25 = int(diameter_axis3.D25)

	def __repr__(self):
		for name, value in vars(DiameterAxis3).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
