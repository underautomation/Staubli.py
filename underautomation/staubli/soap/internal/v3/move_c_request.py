import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveCRequest as move_c_request

class MoveCRequest:
	'''SOAP request for a circular motion command.'''
	def __init__(self, robot: int, frameB: Frame, frameC: Frame, mdesc: MotionDesc, _internal = 0):
		'''Initializes a new instance with the specified parameters.

		:param robot: Robot identifier.
		:param frameB: Intermediate waypoint frame.
		:param frameC: Target frame.
		:param mdesc: Motion description.
		'''
		if(_internal == 0):
			self._instance = move_c_request(robot, frameB, frameC, mdesc)
		else:
			self._instance = _internal

	@property
	def robot(self) -> int:
		'''Robot identifier.'''
		return self._instance.robot

	@robot.setter
	def robot(self, value: int):
		self._instance.robot = value

	@property
	def frame_b(self) -> Frame:
		'''Intermediate waypoint frame.'''
		return Frame(self._instance.frameB)

	@frame_b.setter
	def frame_b(self, value: Frame):
		self._instance.frameB = value._instance if value else None

	@property
	def frame_c(self) -> Frame:
		'''Target frame.'''
		return Frame(self._instance.frameC)

	@frame_c.setter
	def frame_c(self, value: Frame):
		self._instance.frameC = value._instance if value else None

	@property
	def mdesc(self) -> MotionDesc:
		'''Motion description parameters.'''
		return MotionDesc(self._instance.mdesc)

	@mdesc.setter
	def mdesc(self, value: MotionDesc):
		self._instance.mdesc = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MoveCRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
