import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import LengthAxis3 as length_axis3

class LengthAxis3(int):
	Invalid = length_axis3.Invalid
	L100 = length_axis3.L100
	L200 = length_axis3.L200
	L400 = length_axis3.L400
	L600 = length_axis3.L600
