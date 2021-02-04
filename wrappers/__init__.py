# -*- coding: utf-8 -*-
# Copyright: (C) 2014 Bruno Ébé
# Author: Bruno Ébé | contact@brunoebe.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
A common interface to interact with VFX applications.

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


import logging
import importlib

logger = logging.getLogger()

def whatapp():
    appname = None
    # try Houdini
    try:
        import hou
        appname = 'houdini'
    except (ImportError):
    # try Maya
        try:
            import maya
            appname = "maya"
        except (ImportError):
    # try Nuke
            try:
                import nuke
                import nukescripts
                appname = 'nuke'
    # try other apps here
            except (ImportError):
                appname = None

    # return application name
    return appname

def importwrapper():
    app = whatapp()
    if app:
        try:
            logger.debug("Loading %s wrapper..." % (app.capitalize()))
            module = importlib.import_module("."+app, "pyper.wrappers")
            return module.Model()
        except:
            logger.error("Could not load %s wrapper." % (app.capitalize()))
            logger.error("Exiting.")
            return None

