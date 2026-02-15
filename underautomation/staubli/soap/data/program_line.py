import typing
from UnderAutomation.Staubli.Soap.Data import ProgramLine as program_line

class ProgramLine:
	'''Represents a line of a VAL3 program being executed on the controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ProgramLine class.'''
		if(_internal == 0):
			self._instance = program_line()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def application_name(self) -> str:
		'''Name of the application containing the program.'''
		return self._instance.ApplicationName

	@application_name.setter
	def application_name(self, value: str):
		self._instance.ApplicationName = value

	@property
	def program_name(self) -> str:
		'''Name of the program.'''
		return self._instance.ProgramName

	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value

	@property
	def line_number(self) -> int:
		'''Line number currently being executed.'''
		return self._instance.LineNumber

	@line_number.setter
	def line_number(self, value: int):
		self._instance.LineNumber = value

	@property
	def line_content(self) -> str:
		'''Content of the line being executed.'''
		return self._instance.LineContent

	@line_content.setter
	def line_content(self, value: str):
		self._instance.LineContent = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ProgramLine):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
