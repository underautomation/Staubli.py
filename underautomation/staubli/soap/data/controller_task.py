import typing
from underautomation.staubli.soap.data.controller_task_state import ControllerTaskState
from underautomation.staubli.soap.data.program_line import ProgramLine
from UnderAutomation.Staubli.Soap.Data import ControllerTask as controller_task
from UnderAutomation.Staubli.Soap.Data import ControllerTaskState as controller_task_state

class ControllerTask:
	'''Represents a task running on the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ControllerTask class.'''
		if(_internal == 0):
			self._instance = controller_task()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''Name of the task.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def state(self) -> ControllerTaskState:
		'''Current execution state of the task.'''
		return ControllerTaskState(int(self._instance.State))

	@state.setter
	def state(self, value: ControllerTaskState):
		self._instance.State = controller_task_state(int(value))

	@property
	def priority(self) -> int:
		'''Priority level of the task.'''
		return self._instance.Priority

	@priority.setter
	def priority(self, value: int):
		self._instance.Priority = value

	@property
	def created_by(self) -> str:
		'''Name of the entity that created the task.'''
		return self._instance.CreatedBy

	@created_by.setter
	def created_by(self, value: str):
		self._instance.CreatedBy = value

	@property
	def runtime_error(self) -> int:
		'''Runtime error code (0 if no error).'''
		return self._instance.RuntimeError

	@runtime_error.setter
	def runtime_error(self, value: int):
		self._instance.RuntimeError = value

	@property
	def runtime_error_description(self) -> str:
		'''Human-readable description of the runtime error.'''
		return self._instance.RuntimeErrorDescription

	@runtime_error_description.setter
	def runtime_error_description(self, value: str):
		self._instance.RuntimeErrorDescription = value

	@property
	def program_line(self) -> ProgramLine:
		'''Current program line being executed by the task.'''
		return ProgramLine(self._instance.ProgramLine)

	@program_line.setter
	def program_line(self, value: ProgramLine):
		self._instance.ProgramLine = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerTask):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
