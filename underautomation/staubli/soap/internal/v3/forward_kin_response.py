import typing
from underautomation.staubli.soap.data.i_forward_kinematics import IForwardKinematics
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal.V3 import ForwardKinResponse as forward_kin_response

class ForwardKinResponse(IForwardKinematics):
	def __init__(self, position: Frame, config: Config, _internal = 0):
		if(_internal == 0):
			self._instance = forward_kin_response(position, config)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def position(self) -> Frame:
		return Frame(self._instance.Position)
	@position.setter
	def position(self, value: Frame):
		self._instance.Position = value
	@property
	def config(self) -> Config:
		return Config(self._instance.Config)
	@config.setter
	def config(self, value: Config):
		self._instance.Config = value
