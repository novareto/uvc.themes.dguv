# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight
from dolmen.template import ITemplate
from zope import interface
from uvc.design.canvas.menus import IGlobalMenu, IPersonalMenu, INavigationMenu
from uvc.design.canvas.menus import GlobalMenu
from uvc.design.canvas.viewlets import GlobalMenuViewlet
from grokcore.component import adapter, implementer
from . import IDGUVRequest
from dolmen.message import receive
from uvc.design.canvas.managers import IAboveContent


class FlashMessages(uvclight.Viewlet):
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(IAboveContent)
    template = uvclight.get_template('flash.cpt', __file__)

    def update(self):
        self.messages = [msg.message for msg in receive()]

    
class GlobalMenuViewlet(GlobalMenuViewlet):
    uvclight.layer(IDGUVRequest)
    
    def render(self):
        menu = GlobalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


@adapter(IGlobalMenu, interface.Interface)
@implementer(ITemplate)
def global_template(context, request):
    return uvclight.get_template('globalmenu.cpt', __file__)


@adapter(IPersonalMenu, interface.Interface)
@implementer(ITemplate)
def usermenu_template(context, request):
    return uvclight.get_template('usermenu.cpt', __file__)


@adapter(INavigationMenu, interface.Interface)
@implementer(ITemplate)
def nav_template(context, request):
    return uvclight.get_template('navtemplate.cpt', __file__)
