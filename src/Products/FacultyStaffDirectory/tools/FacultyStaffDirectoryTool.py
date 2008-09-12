# -*- coding: utf-8 -*-
#
# File: Repository.py
#
# Copyright (c) 2006 by []
# Generator: ArchGenXML Version 1.5.0 svn/devel
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """WebLion Group <support@weblion.psu.edu>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.FacultyStaffDirectory.config import *
from Products.CMFCore.utils import UniqueObject
from Products.CMFCore.permissions import ModifyPortalContent
from Products.FacultyStaffDirectory.interfaces import IFacultyStaffDirectoryTool, IFacultyStaffDirectoryToolModifiedEvent
from Products.FacultyStaffDirectory.config import MEMBRANE_ABLE_TYPES, MEMBRANE_ABLE_TYPES_VOCAB
from zope.interface import implements
from zope.event import notify
from Products.CMFCore.utils import getToolByName
from Products.membrane.config import TOOLNAME as MEMBRANE_TOOL
import re

Tool_schema = BaseSchema.copy() +Schema((


    StringField(
        name='phoneNumberRegex',
        widget=StringWidget(
            label=u"Phone number format",
            description=u"A regular expression that a Person's phone number must match. Leave blank to disable phone number validation.",
            label_msgid='FacultyStaffDirectory_label_personPhoneNumberFormat',
            description_msgid='FacultyStaffDirectory_description_personPhoneNumberFormat',
            i18n_domain='FacultyStaffDirectory',
            
        ),
        schemata="General",
        default=r"^\(\d{3}\) \d{3}-\d{4}",
    ),

    StringField(
        name='phoneNumberDescription',
        widget=StringWidget(
            label=u"Phone number example",
            description=u"Describe the above phone number rule in a human-readable format: for example, (555) 555-5555.",
            label_msgid='FacultyStaffDirectory_label_personPhoneNumberDescription',
            description_msgid='FacultyStaffDirectory_description_personPhoneNumberDescription',
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="General",
        default=u"(555) 555-5555",
    ),
    
    BooleanField(
        name='obfuscateEmailAddresses',
        widget=BooleanWidget(
            label=u"Custom email obfuscation",
            description=u"Format email addresses like \"someone AT here DOT com\" rather than using Plone's default spam armoring.",
            label_msgid='FacultyStaffDirectory_label_obfuscateEmailAddressesDescription',
            description_msgid='FacultyStaffDirectory_description_obfuscateEmailAddressesDescription',        
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="General",
        default=False,
    ),

    StringField(
        name='idLabel',
        widget=StringWidget(
            label=u"Person ID Label",
            description=u"The name of the ID used by your institution",
            label_msgid='FacultyStaffDirectory_label_personIdLabel',
            description_msgid='FacultyStaffDirectory_description_personIdLabel',
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="Membership",
        default="Access Account ID",
        required=True,
    ),

    StringField(
        name='idRegex',
        widget=StringWidget(
            label=u"Person ID format",
            description=u"A regular expression that a Person's ID must match. Defaults to the value specified in portal_registration.",
            label_msgid='FacultyStaffDirectory_label_personIdFormat',
            description_msgid='FacultyStaffDirectory_description_personIdFormat',            
            i18n_domain='FacultyStaffDirectory',
            
        ),
        schemata="Membership",
        default="",
        required=True,
    ),

    StringField(
        name='idRegexErrorMessage',
        widget=StringWidget(
            label=u"Person ID format error message",
            description=u"The error message returned when the Person ID entered does not match the specified format",
            label_msgid='FacultyStaffDirectory_label_personIdFormatErrorMessage',
            description_msgid='FacultyStaffDirectory_description_personIdFormatErrorMessage',
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="Membership",
        default=u"Invalid user id",
        required=True,
    ),
    
    LinesField(
        name='enableMembraneTypes',
        widget=InAndOutWidget(
            label="Select the content types to integrate with Plone's users and groups",
            description="Integrated types appear on the right; non-integrated on the left. You may move selected items from one column to the other.",
            label_msgid='FacultyStaffDirectory_label_enableMembraneTypes',
            description_msgid='FacultyStaffDirectory_description_enableMembraneTypes',            
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="Membership",
        vocabulary=MEMBRANE_ABLE_TYPES_VOCAB,
        enforceVocabulary=True,
        multiValued=True,
        default=MEMBRANE_ABLE_TYPES,
    ),

    BooleanField(
        name='useInternalPassword',
        widget=BooleanWidget(
            label="Person objects provide user passwords",
            description="Should user passwords be stored as part of the Person? If you're using another PAS plugin to handle authorization, you'll want to turn this off.",
            label_msgid='FacultyStaffDirectory_label_useInternalPassword',
            description_msgid='FacultyStaffDirectory_description_useInternalPassword',
            i18n_domain='FacultyStaffDirectory',
        ),
        schemata="Membership",
        default=True,
    ),
))

Tool_schema['title'].widget.visible = {'edit':'invisible', 'view':'visible'}
Tool_schema['title'].schemata = "metadata"
Tool_schema['id'].schemata = "metadata"

class FacultyStaffDirectoryModifiedEvent(object):
    """Event that happens when edits to a Person have been saved"""
    implements(IFacultyStaffDirectoryToolModifiedEvent)

    def __init__(self, context):
        self.context = context


class FacultyStaffDirectoryTool(UniqueObject, BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(UniqueObject,'__implements__',()),)
    # zope3 interfaces
    implements(IFacultyStaffDirectoryTool)
    # This name appears in the 'add' box
    archetype_name = 'FacultyStaffDirectory Tool'
    meta_type = portal_type = 'FSDFacultyStaffDirectoryTool'
    toolicon = 'group.png'
    global_allow = 0
    _at_rename_after_creation = True
    schema = Tool_schema
    actions = ()
    aliases = {
        '(Default)': 'pre_edit_setup',
        'view': 'pre_edit_setup',
        'index.html': 'pre_edit_setup',
        'edit': 'pre_edit_setup',
        'base_view': 'pre_edit_setup'
    }    
    # tool-constructors have no id argument, the id is fixed
    def __init__(self, id='facultystaffdirectory_tool'):
        BaseContent.__init__(self,id)
        self.setTitle('FacultyStaffDirectory Configuration')
        self.unindexObject()

    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        notify(FacultyStaffDirectoryModifiedEvent(self))
        self.unindexObject()

    security.declareProtected(ModifyPortalContent, 'pre_edit_setup')
    def pre_edit_setup(self):
        """
        """
        # Set the default value for the id regex, based on the settings in portal_registration.
        pr = getToolByName(self, 'portal_registration')
        pattern =  pr.getIDPattern() or pr.getDefaultIDPattern()
        self.schema['idRegex'].default = pattern
        # Force the initial value.
        if not self.getIdRegex():
            self.setIdRegex(pattern)
        # Send to form.    
        return self.facultystaffdirectory_tool_edit()
        
    security.declarePrivate('validate_idRegex')
    def validate_idRegex(self, value):
        """ Make sure that the value entered is a valid regular expression string
        """
        try:
            re.compile(value)
        except:
            return "Invalid regex string."

    security.declarePublic('fsdMemberProfile')
    def fsdMemberProfile(self):
        """Distinguish between an fsd user and a regular acl_users user and
        return the appropriate link for their 'personal profile' page.  For 
        membrane users, this will be the Person object that defines them.  For acl_users
        users it will be 'personalize_form'
        """
        mt = getToolByName(self, 'portal_membership')
        mb = getToolByName(self, MEMBRANE_TOOL)
        
        if not mt.isAnonymousUser():
            usr = mt.getAuthenticatedMember().getUser()
            try:
                foundUser = mb.searchResults(getUserName=usr.getUserName())[0] # grab the first match
                if (foundUser.portal_type == 'FSDPerson'):
                    # this is an FSD Person , get its url and go there
                    url = foundUser.getURL() + '/edit?fieldset=User%20Settings'
                    return url
                else:
                    portalUrl = getToolByName(self,'portal_url')()
                    url = portalUrl + '/personalize_form'
                    return url
            except IndexError:
                portalUrl = getToolByName(self,'portal_url')()
                url = portalUrl + '/personalize_form'
                return url
        
    security.declarePublic('fsdMyFolder')
    def fsdMyFolder(self, id=None):
        """This method attempts to distinguish between a membrane user and a regular
        acl_users user and send them to the appropriate user folder
        """
        mt = getToolByName(self, 'portal_membership')
        mb = getToolByName(self, MEMBRANE_TOOL)
        if id:
            # an id has been passed in, find the user object for that id in acl_users
            usr = mt.getMemberById(id).getUser()
        else:
            usr = mt.getAuthenticatedMember().getUser()
        try:
            foundUser = mb.searchResults(getUserName=usr.getUserName())[0]
            if (foundUser.portal_type == 'FSDPerson'):
                # this is an FSD Person, get its url and go there
                url = foundUser.getURL()
            else:
                # this is a user defined by membrane, but not an FSDPerson, do the regular thing
                url = mt.getHomeUrl(id)
            return url
        except (IndexError, AttributeError):
            # this user is not a membrane user at all, do the regular thing
            url = mt.getHomeUrl(id)
            return url
            
    security.declarePublic('fsdShowMyFolder')
    def fsdShowMyFolder(self, id=None):
        """a test to be used as the condition for the fsdMyFolder action, it will distinguish
        between a membrane user and a non-membrane user, and act accordingly
        """
        mt = getToolByName(self, 'portal_membership')
        mb = getToolByName(self, MEMBRANE_TOOL)
        if id:
            usr = mt.getMemberById(id).getUser()
        else:
            usr = mt.getAuthenticatedMember().getUser()
        try:
            foundUser = mb.searchResults(getUserName=usr.getUserName())[0]
            if (foundUser.portal_type == 'FSDPerson'):
                # this is an FSDPerson, always return true
                return True
            else:
                # this is a membrane user, but not an FSDPerson, check conditions before allowing
                if (mt.getMemberareaCreationFlag() and (mt.getHomeFolder(id) is not None)):
                    return True
                else:
                    return False
        except (IndexError, AttributeError):
            # this is not a membrane user at all, let's check some conditions
            if (mt.getMemberareaCreationFlag() and (mt.getHomeFolder(id) is not None)):
                return True
            else:
                return False
                
        
registerType(FacultyStaffDirectoryTool, PROJECTNAME)
