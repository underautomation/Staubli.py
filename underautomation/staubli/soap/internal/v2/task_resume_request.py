import typing
from UnderAutomation.Staubli.Soap.Internal.V2 import TaskResumeRequest as task_resume_request

class TaskResumeRequest:
	'''SOAP request to resume a suspended task on the controller.'''
	def __init__(self, taskName: str, createdBy: str, _internal = 0):
		'''Initializes a new instance with the specified task name and creator.

		:param taskName: Name of the task to resume.
		:param createdBy: Creator of the task.
		'''
		if(_internal == 0):
			self._instance = task_resume_request(taskName, createdBy)
		else:
			self._instance = _internal

	@property
	def task_name(self) -> str:
		'''Name of the task to resume.'''
		return self._instance.taskName

	@task_name.setter
	def task_name(self, value: str):
		self._instance.taskName = value

	@property
	def created_by(self) -> str:
		'''Creator of the task.'''
		return self._instance.createdBy

	@created_by.setter
	def created_by(self, value: str):
		self._instance.createdBy = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TaskResumeRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
