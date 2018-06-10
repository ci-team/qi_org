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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
        ('You can add links in your config file', '#', 'fab fa-twitter'),
        ('Another social link', '#', 'fab fa-guthub'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS=['images']
THEME='themes/qi'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary']

MARKDOWN = {
    'extensions': ['codehilite(css_class=highlight)',
                   'extra',
                   'admonition',
    ]
}
