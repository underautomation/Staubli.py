import typing
from underautomation.staubli.soap.data.controller_task import ControllerTask
from UnderAutomation.Staubli.Soap.Internal.V2 import GetTasksResponse as get_tasks_response

class GetTasksResponse:
	'''SOAP response containing the list of controller tasks.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the GetTasksResponse class.'''
		if(_internal == 0):
			self._instance = get_tasks_response()
		else:
			self._instance = _internal

	@property
	def tasks(self) -> typing.List[ControllerTask]:
		'''Array of tasks running on the controller.'''
		return [ControllerTask(x) for x in self._instance.Tasks]

	@tasks.setter
	def tasks(self, value: typing.List[ControllerTask]):
		self._instance.Tasks = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, GetTasksResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
