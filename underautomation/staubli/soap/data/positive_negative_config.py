import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PositiveNegativeConfig as positive_negative_config

class PositiveNegativeConfig(int):
	Same = int(positive_negative_config.Same)
	Positive = int(positive_negative_config.Positive)
	Negative = int(positive_negative_config.Negative)
	Free = int(positive_negative_config.Free)

	def __repr__(self):
		for name, value in vars(PositiveNegativeConfig).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
