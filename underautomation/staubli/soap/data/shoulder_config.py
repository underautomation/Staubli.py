import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ShoulderConfig as shoulder_config

class ShoulderConfig(int):
	Same = shoulder_config.Same
	Lefty = shoulder_config.Lefty
	Righty = shoulder_config.Righty
	Free = shoulder_config.Free
