import typing
from underautomation.staubli.soap.data.controller_task_state import ControllerTaskState
from underautomation.staubli.soap.data.program_line import ProgramLine
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ControllerTask as controller_task

class ControllerTask:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_task()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def state(self) -> ControllerTaskState:
		return ControllerTaskState(self._instance.State)
	@state.setter
	def state(self, value: ControllerTaskState):
		self._instance.State = value
	@property
	def priority(self) -> int:
		return self._instance.Priority
	@priority.setter
	def priority(self, value: int):
		self._instance.Priority = value
	@property
	def created_by(self) -> str:
		return self._instance.CreatedBy
	@created_by.setter
	def created_by(self, value: str):
		self._instance.CreatedBy = value
	@property
	def runtime_error(self) -> int:
		return self._instance.RuntimeError
	@runtime_error.setter
	def runtime_error(self, value: int):
		self._instance.RuntimeError = value
	@property
	def runtime_error_description(self) -> str:
		return self._instance.RuntimeErrorDescription
	@runtime_error_description.setter
	def runtime_error_description(self, value: str):
		self._instance.RuntimeErrorDescription = value
	@property
	def program_line(self) -> ProgramLine:
		return ProgramLine(self._instance.ProgramLine)
	@program_line.setter
	def program_line(self, value: ProgramLine):
		self._instance.ProgramLine = value
