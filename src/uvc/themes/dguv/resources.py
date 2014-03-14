# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.bootstrap import bootstrap_js, bootstrap_css


library = Library('uvc.themses.dguv', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_css])
main_js = Resource(library, 'main.js', depends=[bootstrap_js])
