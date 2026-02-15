import typing
from UnderAutomation.Staubli.Soap.Data import Frame as frame

class Frame:
	'''Represents a 3D transformation composed of orientation (a 3x3 rotation matrix) and position (a translation vector) in space. Used to define the pose of a robot or tool in a 3D environment. Matrix representation: [ Nx Ox Ax Px ] [ Ny Oy Ay Py ] [ Nz Oz Az Pz ] [ 0 0 0 1 ]'''
	def __init__(self, _internal = 0):
		'''Default constructor.'''
		if(_internal == 0):
			self._instance = frame()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def nx(self) -> float:
		'''X component of the local X-axis vector (Normal X).'''
		return self._instance.Nx

	@nx.setter
	def nx(self, value: float):
		self._instance.Nx = value

	@property
	def ny(self) -> float:
		'''Y component of the local X-axis vector (Normal Y).'''
		return self._instance.Ny

	@ny.setter
	def ny(self, value: float):
		self._instance.Ny = value

	@property
	def nz(self) -> float:
		'''Z component of the local X-axis vector (Normal Z).'''
		return self._instance.Nz

	@nz.setter
	def nz(self, value: float):
		self._instance.Nz = value

	@property
	def ox(self) -> float:
		'''X component of the local Y-axis vector (Orientation X).'''
		return self._instance.Ox

	@ox.setter
	def ox(self, value: float):
		self._instance.Ox = value

	@property
	def oy(self) -> float:
		'''Y component of the local Y-axis vector (Orientation Y).'''
		return self._instance.Oy

	@oy.setter
	def oy(self, value: float):
		self._instance.Oy = value

	@property
	def oz(self) -> float:
		'''Z component of the local Y-axis vector (Orientation Z).'''
		return self._instance.Oz

	@oz.setter
	def oz(self, value: float):
		self._instance.Oz = value

	@property
	def ax(self) -> float:
		'''X component of the local Z-axis vector (Approach X).'''
		return self._instance.Ax

	@ax.setter
	def ax(self, value: float):
		self._instance.Ax = value

	@property
	def ay(self) -> float:
		'''Y component of the local Z-axis vector (Approach Y).'''
		return self._instance.Ay

	@ay.setter
	def ay(self, value: float):
		self._instance.Ay = value

	@property
	def az(self) -> float:
		'''Z component of the local Z-axis vector (Approach Z).'''
		return self._instance.Az

	@az.setter
	def az(self, value: float):
		self._instance.Az = value

	@property
	def px(self) -> float:
		'''X coordinate of the frame's origin in global space (Pose X).'''
		return self._instance.Px

	@px.setter
	def px(self, value: float):
		self._instance.Px = value

	@property
	def py(self) -> float:
		'''Y coordinate of the frame's origin in global space (Pose Y).'''
		return self._instance.Py

	@py.setter
	def py(self, value: float):
		self._instance.Py = value

	@property
	def pz(self) -> float:
		'''Z coordinate of the frame's origin in global space (Pose Z).'''
		return self._instance.Pz

	@pz.setter
	def pz(self, value: float):
		self._instance.Pz = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Frame):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
