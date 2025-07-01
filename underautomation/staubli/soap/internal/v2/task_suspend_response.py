import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import TaskSuspendResponse as task_suspend_response

class TaskSuspendResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = task_suspend_response()
		else:
			self._instance = _internal
