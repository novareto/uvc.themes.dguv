# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight
from dolmen.template import ITemplate
from zope import interface
from uvc.design.canvas.menus import GlobalMenu
from uvc.design.canvas.viewlets import GlobalMenuViewlet
from grokcore.component import adapter, implementer


class GlobalMenuViewlet(GlobalMenuViewlet):

    def render(self):
        menu = GlobalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


@adapter(GlobalMenu, interface.Interface)
@implementer(ITemplate)
def global_template(context, request):
    return uvclight.get_template('globalmenu.cpt', __file__)
