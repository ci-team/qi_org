#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CI Team'
SITENAME = 'Quantum-Integration.org'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()
# Social widget
SOCIAL = (
        ('@QI_org', 'https://twitter.com/qi_org', 'fab fa-twitter'),
        ('ci-team/qi_org.git', 'https://github.com/ci-team/qi_org', 'fab fa-github'),
        ('Quantum Integration', '#', 'fab fa-medium'),
)

MENUITEMS = (
    ('Home', '/'),
    ('About','/about.html'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS=['images']
THEME='themes/qi'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary','extract_toc']

MARKDOWN = {
    'extensions': ['codehilite(css_class=highlight)',
                   'extra',
                   'admonition',
                   'toc',
    ]
}
