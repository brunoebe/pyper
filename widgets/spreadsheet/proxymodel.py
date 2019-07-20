# -*- coding: utf-8 -*-
# Copyright: (C) 2014-2019 Bruno Ebé
# Author: Bruno Ebé | brunoebe@gmail.com
# License: GNU General Public License v3.0 | https://www.gnu.org/licenses

"""
Module dealing with the widget abstract proxy model.

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


import logging

from pyper.vendor.Qt import QtCore


class ProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, model, parent=None):
        QtCore.QSortFilterProxyModel.__init__(self, parent)
        self._logger = logging.getLogger()

        self.setSourceModel(model)
        self.setDynamicSortFilter(True)
