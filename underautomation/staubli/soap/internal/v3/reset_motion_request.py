import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ResetMotionRequest as reset_motion_request

class ResetMotionRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = reset_motion_request()
		else:
			self._instance = _internal
