import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V2 import TaskResumeRequest as task_resume_request

class TaskResumeRequest:
	def __init__(self, taskName: str, createdBy: str, _internal = 0):
		if(_internal == 0):
			self._instance = task_resume_request(taskName, createdBy)
		else:
			self._instance = _internal
	@property
	def task_name(self) -> str:
		return self._instance.taskName
	@task_name.setter
	def task_name(self, value: str):
		self._instance.taskName = value
	@property
	def created_by(self) -> str:
		return self._instance.createdBy
	@created_by.setter
	def created_by(self, value: str):
		self._instance.createdBy = value
