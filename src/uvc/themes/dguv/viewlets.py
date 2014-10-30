# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight
from . import IDGUVRequest
from dolmen.message import receive
from dolmen.template import ITemplate
from grokcore.component import adapter, implementer
from uvc.content.interfaces import IContent
from uvc.design.canvas import menus, managers
from uvc.design.canvas.viewlets import MenuViewlet
from zope import interface


class ObjectActionMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IAboveContent)
    uvclight.context(IContent)
    uvclight.order(10)
    menu = menus.ContextualActionsMenu
 

class AddMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IAboveContent)
    uvclight.order(20)
    menu = menus.AddMenu


class GlobalMenuViewlet(MenuViewlet):
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(10)
    menu = menus.GlobalMenu

    
class PersonalMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(20)
    menu = menus.PersonalMenu

    
class NavigationMenuViewlet(MenuViewlet):
    uvclight.viewletmanager(managers.IPageTop)
    uvclight.order(30)
    menu = menus.NavigationMenu

    
class FlashMessages(uvclight.Viewlet):
    uvclight.order(2)
    uvclight.layer(IDGUVRequest)
    uvclight.viewletmanager(managers.IAboveContent)
    template = uvclight.get_template('flash.cpt', __file__)

    def update(self):
        self.messages = [msg.message for msg in receive()]


@adapter(menus.IGlobalMenu, interface.Interface)
@implementer(ITemplate)
def global_template(context, request):
    return uvclight.get_template('globalmenu.cpt', __file__)


@adapter(menus.IPersonalMenu, interface.Interface)
@implementer(ITemplate)
def usermenu_template(context, request):
    return uvclight.get_template('usermenu.cpt', __file__)


@adapter(menus.INavigationMenu, interface.Interface)
@implementer(ITemplate)
def nav_template(context, request):
    return uvclight.get_template('navtemplate.cpt', __file__)
