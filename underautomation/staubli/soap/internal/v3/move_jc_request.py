import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from UnderAutomation.Staubli.Soap.Internal.V3 import MoveJCRequest as move_jc_request

class MoveJCRequest:
	'''SOAP request for a joint-to-Cartesian motion command.'''
	def __init__(self, robot: int, frame: Frame, mdesc: MotionDesc, _internal = 0):
		'''Initializes a new instance with the specified parameters.

		:param robot: Robot identifier.
		:param frame: Target Cartesian frame.
		:param mdesc: Motion description.
		'''
		if(_internal == 0):
			self._instance = move_jc_request(robot, frame, mdesc)
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
	def frame(self) -> Frame:
		'''Target Cartesian frame.'''
		return Frame(self._instance.frame)

	@frame.setter
	def frame(self, value: Frame):
		self._instance.frame = value._instance if value else None

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
		if not isinstance(other, MoveJCRequest):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
