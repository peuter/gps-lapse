# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.
import pkg_resources
import os
import logging


class GPSRegistry:
    """ Loads all registered GPS parsers and dispatches the incoming GPS file to the related parser """
    __parsers = {}

    def __init__(self):
        self.log = logging.getLogger(__name__)
        for entry in pkg_resources.iter_entry_points("gpsl.gps.parsers"):
            self.register_parser(entry.name, entry.load())

    def register_parser(self, type, parser):
        self.__parsers[type.lower()] = parser()

    def parse(self, file):
        if not os.path.exists(file):
            self.log.error("gps file '%s' not found" % file)
            return None

        file_type = os.path.splitext(file)[1][1:].lower()
        if file_type not in self.__parsers:
            self.log.error("no parser found for '%s' files" % file_type.upper())
            return None
        else:
            return self.__parsers[file_type].parse(file)

