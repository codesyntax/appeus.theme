from plone.app.contenttypes.interfaces import ICollection
from five import grok

grok.templatedir('templates')


class Home(grok.View):
    grok.context(ICollection)
    grok.require('zope2.View')
    grok.name('home')
