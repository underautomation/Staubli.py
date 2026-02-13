import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import AboveBelowConfig as above_below_config

class AboveBelowConfig(int):
	Same = int(above_below_config.Same)
	Above = int(above_below_config.Above)
	Below = int(above_below_config.Below)
	Free = int(above_below_config.Free)

	def __repr__(self):
		for name, value in vars(AboveBelowConfig).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
