from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from Products.CMFCore.utils import getToolByName

from ex.idmpage import MessageFactory as _

from plone.supermodel import model
#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
import json
import httplib
import urlparse
from zope.component.hooks import getSite

def rolevaluefunc():

    url="https://10.184.39.120:8443/openidm/managed/role"
    domain=urlparse.urlparse(url).netloc
    connection=httplib.HTTPSConnection(domain)
    headers={"X-OpenIDM-Username": "openidm-admin","X-OpenIDM-Password": "openidm-admin"}
    data={"_queryId":"query-all-ids"}
    params=json.dumps(data)
    connection.request("GET",url,params,headers)
    response=connection.getresponse()
    print response.read()
    return response.read()

#def uservalue():
#    membership = getToolByName(context,'portal_membership')
#    currentuser = membership.getAuthenticatedMember()
#    return currentuser


from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName
from zope.interface import directlyProvides

@grok.provider(IContextSourceBinder)
def auser_list(context):
#    mt = getToolByName(context, 'portal_membership')
#    users = mt.listMemberIds()
    users_ldap = context.acl_users.searchPrincipals()
    users=[]
    for i in users_ldap:
        if 'uid' in i.keys():
            users.append(i['uid']) 

    context.plone_log("myusers"+str(users))

    t=[]
    for user in users:
        t.append(SimpleTerm(str(user)))
    return SimpleVocabulary(t)   

def checkrole(value):
    site = getSite()
    membership = getToolByName(site, 'portal_membership')
    currentuser = membership.getAuthenticatedMember()
    site1 = getToolByName(site,'portal_skins')
    a=(site1.custom).readrole(str(currentuser))
    if not (value in a):
        raise Invalid(_(u"You don't have the role"))
    return True

# Interface class; used to define content-type schema.

#class Iidmcontent(form.Schema, IImageScaleTraversable):
class Iidmcontent(model.Schema):
    """
    this is idm content ex
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/idm_content.xml to define the content type.

#    form.model("models/idm_content.xml")
#    uid = schema.TextLine(
#       title=_(u'user name'),
#       defaultFactory=uservalue,
       
#    )
    role = schema.Choice(
       title=_(u"Roles"),
       values=(u"user",u"sailor",u"manager",u"Commander",u"PDI"),
     )   
    auser = schema.Choice(
        title=_(u"User"),
        source=auser_list,
    )    


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class idmcontent(Container):
    grok.implements(Iidmcontent)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# idm_content_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(Iidmcontent)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
