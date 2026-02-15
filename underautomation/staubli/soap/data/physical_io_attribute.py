import typing
from underautomation.staubli.soap.data.physical_aio_attribute import PhysicalAioAttribute
from underautomation.staubli.soap.data.physical_dio_attribute import PhysicalDioAttribute
from UnderAutomation.Staubli.Soap.Data import PhysicalIoAttribute as physical_io_attribute

class PhysicalIoAttribute:
	'''Physical I/O attribute containing either analog or digital specific attributes.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PhysicalIoAttribute class.'''
		if(_internal == 0):
			self._instance = physical_io_attribute()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def aio_attribute(self) -> PhysicalAioAttribute:
		'''Analog I/O specific attributes (null if digital).'''
		return PhysicalAioAttribute(self._instance.AioAttribute)

	@aio_attribute.setter
	def aio_attribute(self, value: PhysicalAioAttribute):
		self._instance.AioAttribute = value._instance if value else None

	@property
	def dio_attribute(self) -> PhysicalDioAttribute:
		'''Digital I/O specific attributes (null if analog).'''
		return PhysicalDioAttribute(self._instance.DioAttribute)

	@dio_attribute.setter
	def dio_attribute(self, value: PhysicalDioAttribute):
		self._instance.DioAttribute = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PhysicalIoAttribute):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
