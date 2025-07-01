import typing
from underautomation.staubli.soap.data.physical_aio_attribute import PhysicalAioAttribute
from underautomation.staubli.soap.data.physical_dio_attribute import PhysicalDioAttribute
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Data import PhysicalIoAttribute as physical_io_attribute

class PhysicalIoAttribute:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = physical_io_attribute()
		else:
			self._instance = _internal
	@property
	def aio_attribute(self) -> PhysicalAioAttribute:
		return PhysicalAioAttribute(self._instance.AioAttribute)
	@aio_attribute.setter
	def aio_attribute(self, value: PhysicalAioAttribute):
		self._instance.AioAttribute = value
	@property
	def dio_attribute(self) -> PhysicalDioAttribute:
		return PhysicalDioAttribute(self._instance.DioAttribute)
	@dio_attribute.setter
	def dio_attribute(self, value: PhysicalDioAttribute):
		self._instance.DioAttribute = value
