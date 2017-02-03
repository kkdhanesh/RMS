## Script (Python) "ws"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
#from Products.PythonScripts.standard import html_quote
#request = container.REQUEST
##response =  request.response

# Return a string identifying this script.
##print "This is the", script.meta_type, '"%s"' % script.getId(),
##if script.title:
##    print "(%s)" % html_quote(script.title),
##print "in", container.absolute_url()


#from Products.CMFCore.utils import getToolByName
#from plone import api

#membership = getToolByName(context,'portal_membership')
#currentuser = membership.getAuthenticatedMember()

#(self.context).manage_setLocalRoles(currentuser, ["PDI"])
#api.user.grant_roles(username=currentuser,roles=["PDI",])
#c=api.user.get_roles(username=currentuser)

#from AccessControl.interfaces import IRoleManager

#if IRoleManager.providedBy(context):
#    context.manage_addLocalRoles(currentuser, ['PDI',])

#cuser=request.form.items()
#cuser=cuser(str(cuser['uid'])
#cuser=request.form['user name']
#cuser=context.uid
cuser=(self.getHistory())[0]['actor']
role=context.role
auser=context.auser

#cuser="senthil"
#context.acl_users.portal_role_manager.assignRoleToPrincipal(role,cuser)
context.acl_users.portal_role_manager.assignRoleToPrincipal(role,auser)
context.plone_log("hello"+str(self))

a=context.readroles(cuser)
try:
    a.remove(role)

    context.roleupdate(cuser,a)
    b=context.readroles(auser)
    b.append(role)
    context.roleupdate(auser,b)

except ValueError:
    pass
   
#print "hello",request.form.items()
#return printed 

#import json
#import httplib
#import base64
#import ssl

#data=json.dumps({  "operation":"replace",  "field":"roles",  "value":["employee"]  })
#c=httplib.HTTPSConnection("10.184.48.199",8443)
#headers = {"Authorization"  : "Basic %s" % base64.b64encode('openidm-admin:openidm-admin'),"Content-Type":"application/json"}
#url="https://10.184.48.199:8443/openidm/managed/user?_action=patch&_queryId=for-userName&uid="+ str(cuser)
#c.request('PUT', url, data, headers=headers)
#q=c.getresponse() 
#context.plone_log("hi"+q)
return

