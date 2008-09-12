from Products.Five import BrowserView
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class PersonView(BrowserView):
    
    @property
    def portrait(self):
        """Return None if no image. 
        
        (tag() field will return an img tag regardless)
        
        """
        return self.context.getImage() and self.context.getWrappedField('image').tag(self.context, scale='normal')
    
    @property
    def officeAddress(self):
        return self.context.getOfficeAddress().replace('\n', '<br />')
        
    @property
    def email(self):
        return self.context.spamProtectFSD(self.context.getEmail())
    

class PersonGalleryViewlet(ViewletBase, PersonView):
    @property
    def portrait(self):
        """Return None if no image. 
        
        (tag() field will return an img tag regardless)
        
        """
        width = self.context.getClassificationViewThumbnailWidth()
        return self.context.getImage() and self.context.getScaledImageByWidth(width)