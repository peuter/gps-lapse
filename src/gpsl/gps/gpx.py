# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.
import gpxpy
import gpxpy.gpx
import logging
from gpsl.gps import TrackParser


class GPXParser(TrackParser):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def parse(self, file):
        res = []
        with open(file, 'r') as gpx_file:
            self.log.debug("parsing %s file" % file)
            gpx = gpxpy.parse(gpx_file)
            self.log.debug("%s tracks found" % len(gpx.tracks))
            for track in gpx.tracks:
                self.log.debug("Track %s has %s segments" % (track.name, len(track.segments)))
                for segment in track.segments:
                    for point in segment.points:
                        self.log.debug('Point from %s at (%s, %s) -> %s' % (point.time, point.latitude, point.longitude, point.elevation))
                        res.append({
                            "lat": point.latitude,
                            "long": point.longitude,
                            "elev": point.elevation,
                            "time": point.time
                        })
        return res


