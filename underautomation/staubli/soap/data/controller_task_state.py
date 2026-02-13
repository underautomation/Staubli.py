import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ControllerTaskState as controller_task_state

class ControllerTaskState(int):
	Idle = int(controller_task_state.Idle)
	Transition = int(controller_task_state.Transition)
	Running = int(controller_task_state.Running)
	Stepping = int(controller_task_state.Stepping)
	Stopped = int(controller_task_state.Stopped)

	def __repr__(self):
		for name, value in vars(ControllerTaskState).items():
			if not name.startswith('_') and isinstance(value, int) and value == self:
				return name
		return str(int(self))
