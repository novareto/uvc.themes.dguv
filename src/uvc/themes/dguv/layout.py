# -*- coding: utf-8 -*-

import uvclight
from zope.interface import Interface
from .resources import main_css, main_js


class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = uvclight.get_template('layout.cpt', __file__)
    base = "/"

    def __call__(self, content, **ns):
        main_css.need()
        main_js.need()
        site = uvclight.getSite()
        self.title = getattr(site, 'title', 'UVCLight')
        if 'view' in ns:
            if hasattr(ns['view'], 'title'):
                self.title = getattr(ns['view'], 'title', u'UVCLight')
        return uvclight.Layout.__call__(self, content, **ns)
