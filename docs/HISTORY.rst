Version History
===============

4.0 (unreleased)
----------------

* Works with Plone 5.0 [vangheem, tkimnguyen]

* Update to not use Products.ATReferenceBrowserWidget
  [vangheem]
  
* Avoid finding extraneous people in classification query
  (e.g. graduate students) by looking up only classifications_people
  relationships [tkimnguyen]


3.1.3 (2012-11-14)
------------------

* Added a MANIFEST.in to exclude the examples folder from being packaged with
  the egg to work around the SandboxViolation from EasyInstall when installing
  FSD via buildout on Windows systems.
  [cah190]

* Work around membrane shortcoming which caused group property providers to
  be enumerated as users, raising an error and preventing further user
  enumeration.
  [Laurence Rowe]


3.1.2 (2012-04-20)
------------------

* Added a 'use site default' option to the available editors list.  Thanks to
  David Carter for reporting this issue and supplying a patch.
  [cah190]

* Require Products.membrane >= 2.1.4 to get the property sheet typing fix which
  affects the ext_editor field.
  [cah190]


3.1.1 (2012-03-28)
------------------

* Added a sample-content profile. [pumazi]

* fsd_atoz_view and department_textual_view should now work on Department objects
  living outside the FacultyStaffDirectory root on a site.  Warning: external
  Departments will only work reliably for situations where there is a single
  FacultyStaffDirectory object in a site.  If there are multiple
  FacultyStaffDirectory objects, then use of external Departments will have
  undefined behavior.
  [cah190]

* Fixes to author.cpt to support Plone 4.x.  Thanks to Paul Roeland for reporting
  this problem and supplying a patch.
  [cah190]

* Fixed fsd_atoz_view to work with last names having first characters outside the
  A to Z range.  We now allow for any valid unicode character.  Thanks to
  Toni Haka-Risku for reporting this problem and supplying a patch which served
  as a starting point for this fix.
  [cah190]


3.1 (2012-03-16)
----------------

* Retagging as 3.1.
  [cah190]


3.1b1 (2011-08-18)
------------------

* Rework templates to reflect the Plone 4.0 layout changes.
  [esteele]

* All FSD content type interfaces now subclass IFacultyStaffDirectoryContent. 
  Q: Why didn't they do so previously?
  A: I have no idea.
  [esteele]

* Drop support for Plone releases below 4.0.
  [esteele]
  
* Remove the reliance on the documentactions viewlet (not shown by default in 
  Plone 4+). vCard link now appears below the contact information in
  person_view.
  [esteele]
  
  
3.0.1
-----

* Add FacultyStaffDirectory to the content types controlled by the FSD Tool's
  activeMembraneStates field. Corrects an issue with customized viewlets 
  failing their permission checks.
  [esteele, pumazi]

* Updated Spanish translation for plone and FacultyStaffDirectory domain
  [macagua (Leonardo J. Caballero G.)]

* Moved the Python import of zope.i18nmessageid to __init__.py and import 
  the MessageFactory for FacultyStaffDirectory domain as FSDMessageFactory
  [macagua (Leonardo J. Caballero G.)]

* Added more support for i18n to "default" profile generic setup.
  [macagua (Leonardo J. Caballero G.)]

3.0
---

* Update person.pt in MobilePhoneExtender to be consistent with FSD's person.pt
  (to fix Plone 4 compatibility).
  [cah190]

* Added missing adapter registration to MobilePhoneExtender.
  [cah190]
  
* activeMembraneStates in the fsdtool now uses a MultiSelectionWidget and the
  workflow states vocabulary.
  [cah190]
  
* Updated course_view.pt for Plone 4.
  [cah190]

3.0b4
-----

* No longer support extenderInstallation install methods.  installExtender and
  installExtenderGloballyIfLocallyIsNotSupported will now throw exceptions.
  uninstallExtender will stay around for at least the 3.0 releases to permit
  easy cleanup of old extender installs.
  [cah190]

* Extender developers should use IBrowserLayerAwareExtender to register their
  extender against a browserlayer to make it possible to activate the extender
  per Plone site.  MobilePhoneExtender has been updated as an example.
  [cah190]

* Drop the icon for the vCard action.
  [esteele]
  
* Slightly rearrange package layout.
  [esteele]
  
* Stop creating a 'my folder' action. This went away in Plone 3.
  [esteele]
  
* Stop using deprecated actionicons_tool and put the icon directly on the action.
  [cah190 (Craig Haynal)]

* Register facultystaffdirectory_tool via GS.
  [cah190 (Craig Haynal)]

* Catalog indexes and metadata are now loaded via GS.
  [cah190 (Craig Haynal)]

* Collection/SmartFolder indexes are now loaded via GS.
  [cah190 (Craig Haynal)]

* Register configlet via GenericSetup.
  [esteele]
  
* Set up navtree properties via GenericSetup.
  [esteele]
  
* Use an import step and GS profile to set up versioning and diffing,
  respectively.
  [esteele]
  
* Reinstall/Refresh is not a Plone supported updating mechanism. Use
  portal_setup instead. Removing the code encouraging this sort of thing.
  [esteele]
  
* Move kupu resource types registration to a GS import step. 
  [esteele]
  
* Drop the 1.0-2.0 migration script. We'll no longer support a direct 1.0-3.0
  migration.
  [esteele]

* Moved css registry manipulation to GS profile, dropped css and js registry
  install code.
  [cah190 (Craig Haynal)]
  
* Install dependencies via GS rather than through Install.py
  [cah190 (Craig Haynal)]
    
* Factory tool registration is now via GS.
  [cah190 (Craig Haynal)]

3.0b3
-----
* Dropped the plone3 GS profile, paved over the types/\*.xml with versions
  from a working FSD Plone instance.
  [cah190 (Craig Haynal)]

* Don't call Products.Archetypes.Extensions.utils helpers, they seem to make
  Archetypes move itself in the portal_skins lists in a way that breaks
  TinyMCE.
  [cah190 (Craig Haynal)]

* Installer should not be installing ATReferenceBrowserWidget.
  [cah190 (Craig Haynal)]

* Register our skins directory the modern way (through ZCML and skins.xml)
  [cah190 (Craig Haynal)]

* Pin to archetypes.schemaextender < 2.1 because 2.1 and higher use plone.uuid
  which breaks Products.Relations and older versions of Archetypes.
  [cah190 (Craig Haynal)]

* Fixed schema conditions and fsdtool data to prevent authorization failures
  for non-managers editing FSD objects.
  [cah190 (Craig Haynal)]

* Updates to facultystaffdirectory_tool access and security
  [cah190 (Craig Haynal)]

* Made FSD not installable when creating a Plone 4 site (our GS profiles are not
  sufficient for a functional install).
  [cah190 (Craig Haynal)]

3.0b2
-----
* Added a lines field to the facultystaffdirectory_tool that contains the list of
  active states.
  [cah190 (Craig Haynal)]

* Inactive users will now fail to authenticate.
  [cah190 (Craig Haynal)]

* Inactive groups will now appear as empty groups.
  [cah190 (Craig Haynal)]

* Fixed author.cpt to work in Plone 4 by adding missing globals.
  [cah190 (Craig Haynal)]

* Replaced direct page template references to facultystaffdirectory_tool with 
  getToolByName lookups to allow for anonymous viewing of listings.
  [cah190 (Craig Haynal)]

* Added missing icon references to GS type information.
  [cah190 (Craig Haynal)]

* Defined global variables (template_id, normalizeString, member) in skin templates.
  [lvb5153 (Luke Brannon)]

* Removed document_action macros from FSD skin templates.
  [lvb5153 (Luke Brannon)]

* Registered document_actions viewlet to abovecontentbody viewlet manager
  for FSD types (in configure.zcml, since there is no browser package).
  [lvb5153 (Luke Brannon)]

* Replaced object_title global definition with context/Title in FSD
  skin templates.
  [lvb5153 (Luke Brannon)]

3.0b1
-----
* Add Plone 4.0 compatibility.
  [ems174, cah190, cewing, netropic]

2.1.5
-----
* Italian translation merged
  (https://weblion.psu.edu/trac/weblion/ticket/1266).
  [cah190 (Craig Haynal)]

* Updated portal_memberdata image generation based on suggestions
  from michael.lindig and updated tests accordingly
  (https://weblion.psu.edu/trac/weblion/ticket/1204).
  [cah190 (Craig Haynal)]

* Fixed Classification's getPeople to account for effective/
  expired, View permissions
  (https://weblion.psu.edu/trac/weblion/ticket/2036)
  [par117 (Paul Rentschler)]

* Added a termination details field and put it and the effective/
  expired dates in a new Employment Information schemata
  [par117 (Paul Rentschler)]

* Updated the person_view.pt file to hide all information except
  the person's name and termination details if they are expired
  unless the viewer has editing rights.
  [par117 (Paul Rentschler)]

2.1.4
-----

* Owner role should be able to edit Persons in Hidden state.
  [ems174 (Eric Steele)]

* Portuguese translation merged.
  [cah190 (Craig Haynal)]

* Allow archetypes.schemaextender 2.x (now includes schema caching).
  [cah190 (Craig Haynal)]

2.1.3
-----

* Fixed the overzealous user search
  (https://weblion.psu.edu/trac/weblion/ticket/842)
  [ems174 (Eric Steele)]

* Revised workflow for Persons. Visibility and membership behavior can
  now be controlled independently.
  [cah190 (Craig Haynal)]

* Fixed an umlaut crash
  (https://weblion.psu.edu/trac/weblion/ticket/1212).
  [ems174 (Eric Steele)]

* Fixed some ReferenceBrowserWidget behavior when running behind a web
  server (https://weblion.psu.edu/trac/weblion/ticket/1222).
  [cah190 (Craig Haynal)]

* Added Turkish translation
  (https://weblion.psu.edu/trac/weblion/ticket/1252).
  [uyar]

* Brought translation infrastructure up to date
  (https://weblion.psu.edu/trac/weblion/ticket/1482).
  [ewr119 (Erik Rose)]

* Corrected the permission needed to manage personnel
  (https://weblion.psu.edu/trac/weblion/ticket/1464).
  [netropic]

* Described the permissions implementations of the Personal
  Assistant(s) field (https://weblion.psu.edu/trac/weblion/ticket/1346).
  [ewr119 (Erik Rose)]

* Wrapped example extender in egg packaging and renamed it.
  [ewr119 (Erik Rose)]

* Fixed syntax error in the French translation.
  [ewr119 (Erik Rose)]

* Included compiled (.mo) versions of all translations.
  [ewr119 (Erik Rose)]

* Fix the getClassificationNames index method so that it doesn't
  throw an error trying to concatenate a function and an int, also
  make sure the method works in 3.2 and 3.3
  [cqp5087 (claytron)]

* Remove MANIFEST.in and use setuptools svn integration instead
  [cqp5087 (claytron)]

2.1.2
-----

* Corrected a problem with the reference browser widget popup not
  displaying available items when used on a site using virtual
  hosting. [ems174 (Eric Steele)]

2.1.1.1
-------

* Corrected a problem with missing files in the 2.1.1 distribution.
  [ems174 (Eric Steele)]

2.1.1
-----

* Corrected a problem with person_view.pt that caused errors
  when anonymous users viewed a person with an assistant
  assigned. [cewing]

* Corrected a problem that prevented versioning of Persons and
  Committees. [cewing]

* Added a dedicated Committees Folder view (similar to the
  specialies folder view). [ajung]

* A Specialty has an extra schemata "Overview" with an image and
  richtext field. Both fields are used for the
  speciality_overview view. [ajung]

* Added microformats for person_view's address block. [robzonenet]

* Added Spanish translation [Gildardo Bautista]

* Added French translation [Benjamin Klups]

* List department in person_view [Gildardo Bautista]

* Corrected a problem with viewing departments located outside
  of a Directory object. [ems174 (Eric Steele)]

2.1
---
* Corrected some CSS display issues with Person pictures.

* Users with the Personnel Manager role can now add Person
  objects.

* Added a field to the classification gallery view to control
  the width of the Person images

* Multiple FacultyStaffDirectory objects can now exist in the
  same site

* Improved product reinstallation performance

* Added an assistant field to confer profile editing delegation
  on other users

* Added a "can manage personnel" field to the sharing tab

* Added i18n hooks for all fields and templates

* Removed a boatload of unused imports

* Removed WebLionLibrary dependency

* Eggified product

* Configlet icon should now work properly in
  VirtualHostMonstered sites

* vCard should handle unicode characters properly now

* vCard images now display

* Empty biographies stay empty

2.0
---

* Added an A-to-Z listing view for Directories and Departments.

* Forced Previous/Next display in the Person editor.

* Bug fixes

2.0a1
-----

* Integrated with Plone users and groups.

* Switched extensibility framework to archetypes.schemaextender.
  More than one extender works at once now, and all content
  types are extensible.

* Added Department content type.

* Sortable Name is now available as a SmartFolder index (mainly
  for sorting).

* Added SmartFolder fields for Departments, Classifications,
  Committees, Specialties, and People.

* Templates are faster.

* Non-ASCII characters in Person titles work.

* People now have a Middle Name field.

* Specialties and other types of person groups can now live
  outside the Faculty/Staff Directory.

* Specialties are now listed in a sane order.

* Committees Folders are now addable within Departments.

* Added a configlet in Site Setup to allow customization of
  phone number and user ID validation as well as the ability
  to disable aspects of membrane integration.

* Silenced some deprecation warnings.

* Added support for Plone 3's versioning.

* Renamed content types to avoid collisions with other products.

* Added oodles of new tests.

* Ditched ArchGenXML, making our code much cleaner.

* Made more use of GenericSetup.

1.0.1 -- Minor documentation tweaks
-----------------------------------

1.0 -- Initial release
----------------------
