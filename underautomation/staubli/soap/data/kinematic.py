import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Kinematic as kinematic

class Kinematic(int):
	Invalid = int(kinematic.Invalid)
	Anthropomorph6 = int(kinematic.Anthropomorph6)
	Anthrioparallel6 = int(kinematic.Anthrioparallel6)
	Anthropomorph5 = int(kinematic.Anthropomorph5)
	Scara = int(kinematic.Scara)
	Eisenmann = int(kinematic.Eisenmann)

	def __repr__(self):
		for name, value in vars(Kinematic).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
