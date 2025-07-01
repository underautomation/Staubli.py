import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import BlendType as blend_type

class BlendType(int):
	BlendOff = blend_type.BlendOff
	BlendJoint = blend_type.BlendJoint
	BlendCartesian = blend_type.BlendCartesian
