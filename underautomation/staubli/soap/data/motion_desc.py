import typing
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.move_type import MoveType
from underautomation.staubli.soap.data.config import Config
from underautomation.staubli.soap.data.blend_type import BlendType
from UnderAutomation.Staubli.Soap.Data import MotionDesc as motion_desc
from UnderAutomation.Staubli.Soap.Data import MoveType as move_type
from UnderAutomation.Staubli.Soap.Data import BlendType as blend_type

class MotionDesc:
	'''Describes the parameters of a robot motion, including tool, frame, velocity, acceleration, blending and configuration.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MotionDesc class.'''
		if(_internal == 0):
			self._instance = motion_desc()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def tool(self) -> Frame:
		'''Defines the pose of the robot's tool center point (TCP) in flange, including both position and orientation.'''
		return Frame(self._instance.Tool)

	@tool.setter
	def tool(self, value: Frame):
		self._instance.Tool = value._instance if value else None

	@property
	def frame(self) -> Frame:
		'''Defines the frame in which the tool position is located, including both position and orientation.'''
		return Frame(self._instance.Frame)

	@frame.setter
	def frame(self, value: Frame):
		self._instance.Frame = value._instance if value else None

	@property
	def abs_rel(self) -> MoveType:
		'''Specifies whether the motion is defined in absolute or relative terms.'''
		return MoveType(int(self._instance.AbsRel))

	@abs_rel.setter
	def abs_rel(self, value: MoveType):
		self._instance.AbsRel = move_type(int(value))

	@property
	def config(self) -> Config:
		'''Contains additional configuration parameters specific to the robot type, such as anthropomorphic, SCARA, or VRBX configurations.'''
		return Config(self._instance.Config)

	@config.setter
	def config(self, value: Config):
		self._instance.Config = value._instance if value else None

	@property
	def blend_type(self) -> BlendType:
		'''Specifies the type of blending to be applied when transitioning between motion segments.'''
		return BlendType(int(self._instance.BlendType))

	@blend_type.setter
	def blend_type(self, value: BlendType):
		self._instance.BlendType = blend_type(int(value))

	@property
	def distance_blend_previous(self) -> float:
		'''In the joint and Cartesian blending modes, the distance between the target point where blending begins and the next point, in millimeters or inches, depending on the length unit used in the application.'''
		return self._instance.DistanceBlendPrevious

	@distance_blend_previous.setter
	def distance_blend_previous(self, value: float):
		self._instance.DistanceBlendPrevious = value

	@property
	def distance_blend_next(self) -> float:
		'''In joint and Cartesian blending modes, the distance between the target point where blending ends and the next point, in millimeters or inches, depending on the length unit of the application.'''
		return self._instance.DistanceBlendNext

	@distance_blend_next.setter
	def distance_blend_next(self, value: float):
		self._instance.DistanceBlendNext = value

	@property
	def velocity(self) -> float:
		'''Maximum allowable joint speed, as a percentage of the robot's nominal speed.'''
		return self._instance.Velocity

	@velocity.setter
	def velocity(self, value: float):
		self._instance.Velocity = value

	@property
	def acceleration(self) -> float:
		'''Maximum allowed joint acceleration, as a percentage of the robot's nominal acceleration.'''
		return self._instance.Acceleration

	@acceleration.setter
	def acceleration(self, value: float):
		self._instance.Acceleration = value

	@property
	def deceleration(self) -> float:
		'''Maximum allowed joint deceleration, as a percentage of the robot's nominal deceleration.'''
		return self._instance.Deceleration

	@deceleration.setter
	def deceleration(self, value: float):
		self._instance.Deceleration = value

	@property
	def translation_velocity(self) -> float:
		'''Maximum allowed feed rate of the tool center, in mm/s or inches/s depending on the length unit of the application.'''
		return self._instance.TranslationVelocity

	@translation_velocity.setter
	def translation_velocity(self, value: float):
		self._instance.TranslationVelocity = value

	@property
	def rotation_velocity(self) -> float:
		'''Maximum permitted tool rotation speed, in degrees per second.'''
		return self._instance.RotationVelocity

	@rotation_velocity.setter
	def rotation_velocity(self, value: float):
		self._instance.RotationVelocity = value

	@property
	def frequency(self) -> float:
		'''Frequency of motion in Hz.'''
		return self._instance.Frequency

	@frequency.setter
	def frequency(self, value: float):
		self._instance.Frequency = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionDesc):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
