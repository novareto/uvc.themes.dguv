# -*- coding: utf-8 -*-

import uvclight
from zope.interface import Interface


class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = uvclight.get_template('layout.cpt', __file__)
    base = "/"
