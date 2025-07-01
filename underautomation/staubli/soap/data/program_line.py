import typing
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import ProgramLine as program_line

class ProgramLine:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = program_line()
		else:
			self._instance = _internal
	@property
	def application_name(self) -> str:
		return self._instance.ApplicationName
	@application_name.setter
	def application_name(self, value: str):
		self._instance.ApplicationName = value
	@property
	def program_name(self) -> str:
		return self._instance.ProgramName
	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value
	@property
	def line_number(self) -> int:
		return self._instance.LineNumber
	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value
	@property
	def line_content(self) -> str:
		return self._instance.LineContent
	@line_content.setter
	def line_content(self, value: str):
		self._instance.LineContent = value
