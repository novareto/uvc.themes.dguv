# -*- coding: utf-8 -*-

import uvclight
from uvclight.interfaces import IBelowContent, IAboveContent
from uvc.design.canvas.views import IHomepage


class SiteMap(uvclight.Viewlet):
    uvclight.order(10)
    uvclight.view(IHomepage)
    uvclight.viewletmanager(IBelowContent)

    template = uvclight.get_template('sitemap.cpt', __file__)
