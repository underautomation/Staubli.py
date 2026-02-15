import typing
from underautomation.staubli.soap.data.i_forward_kinematics import IForwardKinematics
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
from UnderAutomation.Staubli.Soap.Internal.V3 import ForwardKinResponse as forward_kin_response

class ForwardKinResponse(IForwardKinematics):
	'''SOAP response containing the forward kinematics result.'''
	def __init__(self, position: Frame, config: Config, _internal = 0):
		'''Initializes a new instance with the specified position and configuration.

		:param position: Cartesian position.
		:param config: Robot configuration.
		'''
		if(_internal == 0):
			self._instance = forward_kin_response(position, config)
		else:
			self._instance = _internal

	@property
	def position(self) -> Frame:
		'''Cartesian position resulting from forward kinematics.'''
		return Frame(self._instance.Position)

	@position.setter
	def position(self, value: Frame):
		self._instance.Position = value._instance if value else None

	@property
	def config(self) -> Config:
		'''Robot configuration at the computed position.'''
		return Config(self._instance.Config)

	@config.setter
	def config(self, value: Config):
		self._instance.Config = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ForwardKinResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
