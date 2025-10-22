import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import IForwardKinematics as i_forward_kinematics

class IForwardKinematics:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_forward_kinematics()
		else:
			self._instance = _internal
	@property
	def position(self) -> Frame:
		return Frame(self._instance.Position)
	@property
	def config(self) -> Config:
		return Config(self._instance.Config)
