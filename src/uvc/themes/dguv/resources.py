# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.jquery import jquery


library = Library('uvc.themes.dguv', 'static')
main_css = Resource(library, 'main.css', bottom=True)
main_js = Resource(library, 'main.js', depends=[jquery], bottom=True)
