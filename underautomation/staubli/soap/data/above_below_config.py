import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import AboveBelowConfig as above_below_config

class AboveBelowConfig(int):
	Same = above_below_config.Same
	Above = above_below_config.Above
	Below = above_below_config.Below
	Free = above_below_config.Free
