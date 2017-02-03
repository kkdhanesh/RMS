from zope.interface import Interface
from zope import schema
from ex.idmpage import MessageFactory as _

# Adapter interfaces

class IRolestatus(Interface):
    """ Role status can be shown """
    def rstatus():
        """ get role status """
