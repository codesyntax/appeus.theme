from plonetheme.bootstrap.browser.interfaces import IThemeSpecific as IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "APP.EUS Theme" theme, this interface must be its layer
       (in theme/viewlets/configure.zcml).
    """
