from enum import IntEnum

class ControllerTaskState(IntEnum):
	'''Execution state of a controller task.'''
	Idle = 0 # Task is idle and not executing.
	Transition = 1 # Task is transitioning between states.
	Running = 2 # Task is currently running.
	Stepping = 3 # Task is executing step by step.
	Stopped = 4 # Task is stopped.
