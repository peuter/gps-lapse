# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.
from setproctitle import setproctitle
from argparse import ArgumentParser
import os
from gpsl.env import Environment
from gpsl.gps.registry import GPSRegistry
import logging

VERSION = __import__('pkg_resources').get_distribution('gpsl').version


def main():
    setproctitle("gps-lapse")
    parser = ArgumentParser(usage="%(prog)s - GPS-lapse commands")
    parser.add_argument("--version", action='version', version=VERSION)
    parser.add_argument("--pics", "-p", dest="pics", help="Source directory for the pictures")
    parser.add_argument("--gps", "-g", dest="gps_file", help="GPS file to use")
    parser.add_argument("--out", "-o", default="./", dest="output_dir", help="Output directory")
    parser.add_argument("--file", "-f", default="lapse.mp4", dest="file_name", help="Output video file name")
    parser.add_argument("--config", "-c", dest="config", default=os.environ.get('GPSL_CONFIG_DIR') or "/etc/gpsl",
                        help="read configuration from DIRECTORY [%(default)s]",
                        metavar="DIRECTORY")

    options, unknown = parser.parse_known_args()
    Environment.config_dir = options.config
    env = Environment.getInstance()
    log = logging.getLogger(__name__)

    gps_parser_registry = None
    if options.gps_file is not None:
        gps_parser_registry = GPSRegistry()
        parsed_gps = gps_parser_registry.parse(options.gps_file)
        log.info(parsed_gps)

    logging.shutdown()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(name)s - %(message)s')
    main()
