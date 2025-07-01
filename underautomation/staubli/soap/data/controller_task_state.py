import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ControllerTaskState as controller_task_state

class ControllerTaskState(int):
	Idle = controller_task_state.Idle
	Transition = controller_task_state.Transition
	Running = controller_task_state.Running
	Stepping = controller_task_state.Stepping
	Stopped = controller_task_state.Stopped
