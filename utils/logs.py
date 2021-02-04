# -*- coding: utf-8 -*-
# Copyright: (C) 2014 Bruno Ébé
# Author: Bruno Ébé | contact@brunoebe.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
Module gathering logging related functions.

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
import logging
import logging.config


def setup_logging(configFile, filename="~/.logging.log"):
    """convenience function to setup the logger"""
    if os.path.exists(configFile):
        # expand any os variable like "~"
        filename = os.path.expanduser(filename)
        filename = os.path.expandvars(filename)

        # create the application directory if it does not exist
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # creates the output file if it does not exist
        open(filename, "a").close()

        # load the configuration file and pass the output file
        logging.config.fileConfig(configFile, defaults={"logfilename": filename}, disable_existing_loggers=False)

    else:
        # if no config file exist, use the basic configuration from the logging module
        logging.basicConfig(level=logging.INFO)
        logging.warning("No logging configuration file found: using basic configuration.")
        
    logger = logging.getLogger(__name__)
    return logger

