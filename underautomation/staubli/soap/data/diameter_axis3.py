import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import DiameterAxis3 as diameter_axis3

class DiameterAxis3(int):
	Invalid = diameter_axis3.Invalid
	D20 = diameter_axis3.D20
	D25 = diameter_axis3.D25
