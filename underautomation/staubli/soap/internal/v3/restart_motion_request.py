import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import RestartMotionRequest as restart_motion_request

class RestartMotionRequest:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = restart_motion_request()
		else:
			self._instance = _internal
