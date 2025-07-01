import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ValApplication as val_application

class ValApplication:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = val_application()
		else:
			self._instance = _internal
	@property
	def name(self) -> str:
		return self._instance.Name
	@name.setter
	def name(self, value: str):
		self._instance.Name = value
	@property
	def loaded(self) -> bool:
		return self._instance.Loaded
	@loaded.setter
	def loaded(self, value: bool):
		self._instance.Loaded = value
	@property
	def is_crypted(self) -> bool:
		return self._instance.IsCrypted
	@is_crypted.setter
	def is_crypted(self, value: bool):
		self._instance.IsCrypted = value
	@property
	def is_running(self) -> bool:
		return self._instance.IsRunning
	@is_running.setter
	def is_running(self, value: bool):
		self._instance.IsRunning = value
