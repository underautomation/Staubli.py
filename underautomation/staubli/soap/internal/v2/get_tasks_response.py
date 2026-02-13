import typing
from underautomation.staubli.soap.data.controller_task import ControllerTask
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import GetTasksResponse as get_tasks_response

class GetTasksResponse:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = get_tasks_response()
		else:
			self._instance = _internal
	@property
	def tasks(self) -> typing.List[ControllerTask]:
		return [ControllerTask(x) for x in self._instance.Tasks]
	@tasks.setter
	def tasks(self, value: typing.List[ControllerTask]):
		self._instance.Tasks = value._instance if value else None
