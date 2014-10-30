# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.jquery import jquery
from js.bootstrap import bootstrap_js, bootstrap_css

library = Library('uvc.themes.dguv', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_css])
main_js = Resource(library, 'main.js', depends=[jquery, bootstrap_js])
