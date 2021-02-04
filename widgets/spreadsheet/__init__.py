# -*- coding: utf-8 -*-
# Copyright: (C) 2014 Bruno Ébé
# Author: Bruno Ebé | contact@brunoebe.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
A widget example that display a list of parameters as spreadsheets.

Copyright: (C) 2014 Bruno Ébé
Author: Bruno Ebé | contact@brunoebe.com
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

from pyper.__about__ import *
import pyper.utils as utils
import pyper.wrappers as wrappers
from . import ui

# import importlib
# importlib.reload(utils) # @debug: reload the module for development convenience
# importlib.reload(wrappers) # @debug: reload the module for development convenience
# importlib.reload(ui) # @debug: reload the module for development convenience


## global variables
LOGGING_CONFIG_FILE = 'config/logging.ini'
LOGGING_LOG_FILE = '~/.%s/logging.log' % __name__
NAME = __name__.split('.')[-1].capitalize()


def run():
    """main run function"""

    application = wrappers.whatapp()

    # load and configure the logging module
    configFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), LOGGING_CONFIG_FILE)
    logger = utils.logs.setup_logging(configFile, LOGGING_LOG_FILE)

    # start initialization
    logger.info("Initializing %s..." % (NAME))

    # Load the application wrapper
    wrapper = wrappers.importwrapper()
    if not wrapper:
        logger.error("Could not load wrapper %s." % (NAME))
        logger.error("Exiting.")
        return

    # Build the UI with the wrapper
    widget = ui.MainWidget(wrapper)
    if not widget:
        logger.error("Could not build %s's widget." % (NAME))
        logger.error("Exiting.")
        return

    # Show the widget
    widget.show()
    logger.debug("%s's interface has been created: %s" % (NAME, widget))
    logger.info("Running %s in %s." % (NAME, wrapper.name.capitalize()))

    # return the widget in case it is needed 
    return widget
