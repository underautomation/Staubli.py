import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import Frame as frame

class Frame:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = frame()
		else:
			self._instance = _internal
	@property
	def nx(self) -> float:
		return self._instance.Nx
	@nx.setter
	def nx(self, value: float):
		self._instance.Nx = value
	@property
	def ny(self) -> float:
		return self._instance.Ny
	@ny.setter
	def ny(self, value: float):
		self._instance.Ny = value
	@property
	def nz(self) -> float:
		return self._instance.Nz
	@nz.setter
	def nz(self, value: float):
		self._instance.Nz = value
	@property
	def ox(self) -> float:
		return self._instance.Ox
	@ox.setter
	def ox(self, value: float):
		self._instance.Ox = value
	@property
	def oy(self) -> float:
		return self._instance.Oy
	@oy.setter
	def oy(self, value: float):
		self._instance.Oy = value
	@property
	def oz(self) -> float:
		return self._instance.Oz
	@oz.setter
	def oz(self, value: float):
		self._instance.Oz = value
	@property
	def ax(self) -> float:
		return self._instance.Ax
	@ax.setter
	def ax(self, value: float):
		self._instance.Ax = value
	@property
	def ay(self) -> float:
		return self._instance.Ay
	@ay.setter
	def ay(self, value: float):
		self._instance.Ay = value
	@property
	def az(self) -> float:
		return self._instance.Az
	@az.setter
	def az(self, value: float):
		self._instance.Az = value
	@property
	def px(self) -> float:
		return self._instance.Px
	@px.setter
	def px(self, value: float):
		self._instance.Px = value
	@property
	def py(self) -> float:
		return self._instance.Py
	@py.setter
	def py(self, value: float):
		self._instance.Py = value
	@property
	def pz(self) -> float:
		return self._instance.Pz
	@pz.setter
	def pz(self, value: float):
		self._instance.Pz = value
