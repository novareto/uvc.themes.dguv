# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.jquery import jquery
from os.path import join


library = Library('uvc.themes.dguv', 'static')
datepicker = Library('datepicker', join('static', 'datetime_picker'))

main_css = Resource(library, 'main.css', bottom=True)
main_js = Resource(library, 'main.js', depends=[jquery], bottom=True)

moment = Resource(
    datepicker, 'moment.js')
datepjs = Resource(
    datepicker, 'bootstrap-datetimepicker.min.js', depends=[main_js, moment])
datepcss = Resource(
    datepicker, 'bootstrap-datetimepicker.min.css')

dateputils = Resource(
    datepicker, 'gk.js', depends=[datepcss, datepjs])


alldate = Resource(
    datepicker, 'alldate.js', depends=[dateputils])
