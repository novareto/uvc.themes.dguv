# -*- coding: utf-8 -*-

import uvclight
from uvc.design.canvas.menus import INavigationMenu


class SomeEntry(uvclight.MenuItem):
    uvclight.title(u'Passwort ändern')
    uvclight.auth.require('zope.Public')
    uvclight.menu(INavigationMenu)

    @property
    def action(self):
       return self.view.url(self.context)
