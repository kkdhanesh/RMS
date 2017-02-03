from five import grok
from ex.idmpage.idm_content import Iidmcontent
from ex.idmpage.interfaces import IRolestatus

# Viewlet

from zope.component import getMultiAdapter
from plone.app.layout.viewlets.interfaces import IBelowContentTitle
from plone.app.layout.globals.interfaces import IViewView

class RolestatusIDM(grok.Adapter):
    """ get role status """
    grok.provides(IRolestatus)
    grok.context(Iidmcontent)

    def __init__(self, context):
        self.context = context

##class RolestatusViewlet(grok.Viewlet):
##    """ viewlet for displaying role status """
##    grok.context(Iidmcontent)
##    grok.view(IViewView)
##    grok.viewletmanager(IBelowContentTitle)
##    grok.name('ex.idmpage.rolestatus')
##    grok.require('zope2.View')
   
#    grok.template('ratings_templates/ratingsviewlet.pt')
#    grok.template('ratingsviewlet.pt')

    def update(self):
        self.rolestatus = IRolestatus(self.context)
                 
#   def render(self):
#       self.render()
#       render=ViewPageTemplateFile('ratings_templates/ratingsviewlet.pt')
    

