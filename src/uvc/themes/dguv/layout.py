# -*- coding: utf-8 -*-

import uvclight
from zope.interface import Interface
from . import IDGUVRequest
from .resources import main_css, main_js



class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = uvclight.get_template('layout.cpt', __file__)
    base = "/"
    title = u"Some title"

    def __call__(self, content, **ns):
        main_css.need()
        main_js.need()
        return uvclight.Layout.__call__(self, content, **ns)
