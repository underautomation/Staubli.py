import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import BlendType as blend_type

class BlendType(int):
	BlendOff = int(blend_type.BlendOff)
	BlendJoint = int(blend_type.BlendJoint)
	BlendCartesian = int(blend_type.BlendCartesian)

	def __repr__(self):
		for name, value in vars(BlendType).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
