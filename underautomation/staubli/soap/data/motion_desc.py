import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.move_type import MoveType
from underautomation.staubli.soap.data.config import Config
from underautomation.staubli.soap.data.blend_type import BlendType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import MotionDesc as motion_desc
from UnderAutomation.Staubli.Soap.Data import MoveType as move_type
from UnderAutomation.Staubli.Soap.Data import BlendType as blend_type

class MotionDesc:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_desc()
		else:
			self._instance = _internal
	@property
	def tool(self) -> Frame:
		return Frame(self._instance.Tool)
	@tool.setter
	def tool(self, value: Frame):
		self._instance.Tool = value._instance if value else None
	@property
	def frame(self) -> Frame:
		return Frame(self._instance.Frame)
	@frame.setter
	def frame(self, value: Frame):
		self._instance.Frame = value._instance if value else None
	@property
	def abs_rel(self) -> MoveType:
		return MoveType(self._instance.AbsRel)
	@abs_rel.setter
	def abs_rel(self, value: MoveType):
		self._instance.AbsRel = move_type(int(value))
	@property
	def config(self) -> Config:
		return Config(self._instance.Config)
	@config.setter
	def config(self, value: Config):
		self._instance.Config = value._instance if value else None
	@property
	def blend_type(self) -> BlendType:
		return BlendType(self._instance.BlendType)
	@blend_type.setter
	def blend_type(self, value: BlendType):
		self._instance.BlendType = blend_type(int(value))
	@property
	def distance_blend_previous(self) -> float:
		return self._instance.DistanceBlendPrevious
	@distance_blend_previous.setter
	def distance_blend_previous(self, value: float):
		self._instance.DistanceBlendPrevious = value
	@property
	def distance_blend_next(self) -> float:
		return self._instance.DistanceBlendNext
	@distance_blend_next.setter
	def distance_blend_next(self, value: float):
		self._instance.DistanceBlendNext = value
	@property
	def velocity(self) -> float:
		return self._instance.Velocity
	@velocity.setter
	def velocity(self, value: float):
		self._instance.Velocity = value
	@property
	def acceleration(self) -> float:
		return self._instance.Acceleration
	@acceleration.setter
	def acceleration(self, value: float):
		self._instance.Acceleration = value
	@property
	def deceleration(self) -> float:
		return self._instance.Deceleration
	@deceleration.setter
	def deceleration(self, value: float):
		self._instance.Deceleration = value
	@property
	def translation_velocity(self) -> float:
		return self._instance.TranslationVelocity
	@translation_velocity.setter
	def translation_velocity(self, value: float):
		self._instance.TranslationVelocity = value
	@property
	def rotation_velocity(self) -> float:
		return self._instance.RotationVelocity
	@rotation_velocity.setter
	def rotation_velocity(self, value: float):
		self._instance.RotationVelocity = value
	@property
	def frequency(self) -> float:
		return self._instance.Frequency
	@frequency.setter
	def frequency(self, value: float):
		self._instance.Frequency = value
