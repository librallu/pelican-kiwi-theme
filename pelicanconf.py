#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Your Name here'
SITENAME = u'Pelican Kiwi Theme - Demo'
SITEURL = '' # PUT THE BASE URL HERE
# SITEURL = 'http://librallu.github.io/pelican-kiwi-theme'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME='dest/kiwi/'

KIWI_EDITO_IMAGE_LINK = SITEURL+'/images/avatar.png'
KIWI_EDITO_IMAGE_ALT = 'It is me !'
KIWI_EDITO_TITLE = 'About me'
KIWI_EDITO_TEXT = """
Donec tempor ullamcorper vulputate. Vestibulum tristique mi arcu, in semper diam sagittis vitae. Donec aliquam enim in magna elementum, vel blandit quam suscipit.
"""

# FOR SEO
BLOG_DESCRIPTION = "Pelican Kiwi Theme demo page"

SOCIAL = [
    ('twitter', 'librallu'),
    ('github', 'librallu')
]

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
