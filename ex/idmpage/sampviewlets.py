from plone.app.layout.viewlets import ViewletBase
from datetime import datetime
from Products.CMFCore.utils import getToolByName

#CONFERENCE_START_DATE = datetime(2015, 10, 12)
#usname="abcd"
#role="efgh"



##commented the following-this works for data object id retrieving only
#import json
#import httplib
#import base64
#import ssl                 
#c=httplib.HTTPSConnection("10.184.49.227",8443)
#headers = {"Authorization"  : "Basic %s" % base64.b64encode('openidm-admin:openidm-admin')}
#url="https://10.184.49.227:8443/openidm/managed/user?_queryId=query-all-ids&_prettyPrint=true"
#c.request('GET', url, headers=headers)
#q=c.getresponse()
#l=q.read()
#l2=json.loads(l)
#u=[i['_id'].decode('unicode_escape').encode('ascii','ignore') for i in l2['result']]
#roles=u

import json
import httplib
import base64
import ssl


class DaysToConferenceViewlet(ViewletBase):

    def date(self):
#        return CONFERENCE_START_DATE
#        return usname,role

        membership = getToolByName(self.context,'portal_membership')
        currentuser = membership.getAuthenticatedMember()



        c=httplib.HTTPSConnection("10.184.48.199",8443)
        headers = {"Authorization"  : "Basic %s" % base64.b64encode('openidm-admin:openidm-admin')}
        url="https://10.184.48.199:8443/openidm/managed/user?_queryFilter=userName%20eq%20%22"+ str(currentuser) + "%22"
        c.request('GET', url, headers=headers)
        q=c.getresponse()
        l=q.read()
        l2=json.loads(l)
        try:
            self.context.plone_log("hi"+str(len(l2['result'][0]['roles'])))
            u=[i.decode('unicode_escape').encode('ascii','ignore') for i in l2['result'][0]['roles']]
            roles=u
#        c=(self.context).get_local_roles()

        except keyError:
            roles=[]
        c.close()
        return roles

