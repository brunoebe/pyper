# -*- coding: utf-8 -*-
# Copyright: (C) 2014 Bruno Ébé
# Author: Bruno Ébé | contact@brunoebe.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
Wrapper to interact with Maya application.

Copyright: (C) 2014 Bruno Ébé
Author: Bruno Ébé | contact@brunoebe.com
License:
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import os
import sys
import logging
import importlib

from pyper.__about__ import *

# import base class
from . import standalone 


class Model(standalone.Model):
    """ Model derived for Maya from the base class 'standalone.Model'. """
    
    name = "Maya"

    def __init__(self):
        standalone.Model.__init__(self)
        
        # import maya commands
        self._mayamodule = importlib.import_module("maya.cmds")

        # initialize logger
        self._logger = logging.getLogger()
        self._iconpath = ""

        # define main parent window
        self.mainQtWindow = None

    def translatePath(self, path):
        """
        convenient function to allow each package to convert a
        unix style path to it's own path format
        for instance maya uses "|"
        """
        return path.replace("/", "|")

    def hasParameter(self, path):
        if self.parmCount(path):
            return True
        return False

    def parmCount(self, path):
        return len(self.getParms(path))

    def isParameter(self, path):
        try:
            return maya.attributeQuery(path.split(".")[-1], n=path.split(".")[0], exists=True)
        except:
            return False

    def childCount(self, path):
        return len(self.getChildren(path))

    def getName(self, path):
        res = ""

        if path == "|": 
            path = "|*"
            res = "|"

        ls = self._mayamodule.ls(path)
        if ls: res = ls[0].split('.')[-1]

        return res

    def getPath(self, path):
        res = ""

        if path == "|": 
            path = "|*"
            res = "|"

        ls = self._mayamodule.ls(path, long=True)
        if ls: res = ls[0]

        return res

    def getChildren(self, path):
        res = []

        if path:
            if path == "|":
                return self._mayamodule.ls("|*")
            res = self._mayamodule.listRelatives(path, children=True, fullPath=True)

        if not res:
            res = []

        return res

    def getParms(self, path):
        try:
            return ["%s.%s" % (path, str(a)) for a in self._mayamodule.listAttr(path)]
        except:
            return []

    def evalAsString(self, path):
        try:
            return str(self._mayamodule.getAttr(path))
        except:
            return ""

    def hasChild(self, path):
        if self.childCount(path):
            return True
        return False

    def type(self, path):
        if path == "|":
            return ""
        return self._mayamodule.objectType(path)

    def icon(self, path):

        if self.isParameter(path):
            return ""

        # for now return empty path
        return ""

    def selection(self):
        return self._mayamodule.ls(sl=True, long=True)

    def setParms(self, parms={}):
        pass
