import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
from UnderAutomation.Staubli.Soap.Data import IForwardKinematics as i_forward_kinematics

class IForwardKinematics:
	'''Represents the result of a forward kinematics computation.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_forward_kinematics()
		else:
			self._instance = _internal

	@property
	def position(self) -> Frame:
		'''Cartesian position resulting from the forward kinematics computation.'''
		return Frame(self._instance.Position)

	@property
	def config(self) -> Config:
		'''Robot configuration associated with the computed position.'''
		return Config(self._instance.Config)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IForwardKinematics):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
