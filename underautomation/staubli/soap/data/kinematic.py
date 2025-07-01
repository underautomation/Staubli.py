import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Kinematic as kinematic

class Kinematic(int):
	Invalid = kinematic.Invalid
	Anthropomorph6 = kinematic.Anthropomorph6
	Anthrioparallel6 = kinematic.Anthrioparallel6
	Anthropomorph5 = kinematic.Anthropomorph5
	Scara = kinematic.Scara
	Eisenmann = kinematic.Eisenmann
