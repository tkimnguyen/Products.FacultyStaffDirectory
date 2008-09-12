# -*- coding: utf-8 -*-

__author__ = """WebLion <support@weblion.psu.edu>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.CMFCore.permissions import View
from Products.FacultyStaffDirectory.PersonGrouping import PersonGrouping
from Products.Relations.field import RelationField
from Products.FacultyStaffDirectory.config import *
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from Products.membrane.interfaces import IPropertiesProvider
from Products.FacultyStaffDirectory.interfaces import ICommittee, IGroupingProvidingMembership
from Acquisition import aq_inner, aq_parent
from Products.FacultyStaffDirectory.permissions import ASSIGN_COMMITTIES_TO_PEOPLE

schema = Schema((

    RelationField(
        name='members',
        widget=ReferenceBrowserWidget(
            label=u'Members',
            label_msgid='FacultyStaffDirectory_label_members',
            i18n_domain='FacultyStaffDirectory',
            base_query={'portal_type':'FSDPerson', 'sort_on':'getSortableName'},
            allow_browse=0,
            allow_search=1,
            show_results_without_query=1,
        ),
        write_permission = ASSIGN_COMMITTIES_TO_PEOPLE,
        allowed_types=('FSDPerson',),
        multiValued=True,
        relationship='CommitteeMembership'
    ),
),
)

Committee_schema = getattr(PersonGrouping, 'schema', Schema(())).copy() + schema.copy()

class Committee(PersonGrouping):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(PersonGrouping,'__implements__',()),)
    # zope3 interfaces
    implements(ICommittee, IPropertiesProvider, IGroupingProvidingMembership)
    meta_type = portal_type = 'FSDCommittee'
    _at_rename_after_creation = True
    schema = Committee_schema
    # Methods
    security.declareProtected(View, 'getMembershipInformation')
    def getMembershipInformation(self, person):
        """ Get the committee membership information for a specific person
        """
        refCatalog = getToolByName(self, 'reference_catalog')
        refs = refCatalog.getReferences(self, 'CommitteeMembership', person)

        if not refs:
            return None
        else:
            return refs[0].getContentObject()

    security.declareProtected(View, 'getPeople')
    def getPeople(self):
        """ Return the people in this committee.
            Mainly for context-sensitive classifications
        """
        return self.getMembers()

    security.declareProtected(View, 'getRawPeople')
    def getRawPeople(self):
        """ Return the people associations associated with this committee
        """
        return self.getRawMembers()

    #
    # Validators
    #
    security.declarePrivate('validate_id')
    def validate_id(self, value):
        """Ensure the id is unique, also among groups globally
        """
        if value != self.getId():
            parent = aq_parent(aq_inner(self))
            if value in parent.objectIds():
                return "An object with id '%s' already exists in this folder" % value
        
            groups = getToolByName(self, 'portal_groups')
            if groups.getGroupById(value) is not None:
                return "A group with id '%s' already exists in the portal" % value

registerType(Committee, PROJECTNAME)
# end of class Committee

