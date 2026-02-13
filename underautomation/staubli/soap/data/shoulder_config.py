import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ShoulderConfig as shoulder_config

class ShoulderConfig(int):
	Same = int(shoulder_config.Same)
	Lefty = int(shoulder_config.Lefty)
	Righty = int(shoulder_config.Righty)
	Free = int(shoulder_config.Free)

	def __repr__(self):
		for name, value in vars(ShoulderConfig).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
