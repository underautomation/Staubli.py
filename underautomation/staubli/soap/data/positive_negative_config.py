import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PositiveNegativeConfig as positive_negative_config

class PositiveNegativeConfig(int):
	Same = positive_negative_config.Same
	Positive = positive_negative_config.Positive
	Negative = positive_negative_config.Negative
	Free = positive_negative_config.Free
