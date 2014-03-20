# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from uvc.basetheme import css as basecss
from js.jquery import jquery
from js.bootstrap import bootstrap_js

library = Library('uvc.themes.dguv', 'static')
main_css = Resource(library, 'main.css', depends=[basecss])
main_js = Resource(library, 'main.js', depends=[jquery, bootstrap_js])
