# -*- coding: utf-8 -*-
# This file is a part of MediaCore CE, Copyright 2009-2012 MediaCore Inc.
# The source code in this file is dual licensed under the MIT license or the 
# GPL version 3 or (at your option) any later version.
# See LICENSE.txt in the main project directory, for more information.
#
# Copyright (c) 2012 Felix Schwarz (www.schwarz.eu)

from mediacore.lib.js_delivery import ResourcesCollection

__all__ = ['StyleSheet', 'StyleSheets']

class StyleSheet(object):
    def __init__(self, url, key=None):
        self.url = url
        self.key = key
    
    def __unicode__(self):
        return '<link href="%s" rel="stylesheet" type="text/css"></link>' % self.url
    
    def __repr__(self):
        return 'StyleSheet(%r, key=%r)' % (self.url, self.key)
    
    def __eq__(self, other):
        if not hasattr(other, 'url'):
            return False
        return self.url == other.url
    
    def __ne__(self, other):
        return not (self == other)


class StyleSheets(ResourcesCollection):
    def add(self, stylesheet):
        if stylesheet in self._resources:
            return
        self._resources.append(stylesheet)
    
    # --- some interface polishing ---------------------------------------------
    @property
    def stylesheets(self):
        return self._resources
    
    def replace_stylesheet_with_key(self, stylesheet):
        self.replace_resource_with_key(stylesheet)

