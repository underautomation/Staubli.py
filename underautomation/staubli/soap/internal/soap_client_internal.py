import typing
from underautomation.staubli.soap.internal.soap_client_base import SoapClientBase
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal import SoapClientInternal as soap_client_internal

class SoapClientInternal(SoapClientBase):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_client_internal()
		else:
			self._instance = _internal
