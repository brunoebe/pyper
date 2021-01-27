# -*- coding: utf-8 -*-
# Copyright: (C) 2014-2019 Bruno Ebé
# Author: Bruno Ebé | brunoebe@gmail.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
Wrapper to allow widgets to run standalone.

Copyright: (C) 2014-2019 Bruno Ebé
Author: Bruno Ebé | brunoebe@gmail.com
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

from pyper.__about__ import *


class Model(object):
    """ docstring for StandaloneModel """

    name = "Standalone"

    def __init__(self):
        pass

    def childCount(self, path):
        pass

    def evalAsString(self, path):
        pass

    def getName(self, path):
        pass

    def getPath(self, path):
        pass

    def getChildren(self, path):
        return [""]

    def getHoudiniObject(self, path):
        pass

    def getParms(self, path):
        pass

    def hasChild(self, path):
        pass

    def hasParameter(self, path):
        pass

    def icon(self, path):
        pass

    def isParameter(self, path):
        pass

    def parmCount(self, path):
        pass

    def playblast(self, outputName):
        pass

    def selection(self):
        pass

    def setParms(self, parms=[]):
        pass

    def translatePath(self, path):
        """
        convenient function to allow each package to convert a
        unix style path to it's own path format
        for instance: maya uses "|", houdini uses "/"
        """
        return path

    def type(self, path):
        pass