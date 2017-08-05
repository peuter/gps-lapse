# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.

__import__('pkg_resources').declare_namespace(__name__)


class TrackParser:
    """ Interface for GPS track file parsers """

    def parse(self, file):
        """
        Parse a file with GPS track data and return a dictionary with this content

        .. code-block:: none

            [{
                "lat": <latitute> [float]
                "long": <longitude> [float]
                "time": <datetime>  [datetime.datetime]
                "elev": <elevation> [float?]
            },..
            ]

        :param file: path to file with gps track data
        :type file: string
        :return: dict with all points found in the file
        :rtype: dict
        """
        raise NotImplementedError