# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.

VERSION = __import__('pkg_resources').get_distribution('gpsl').version
__import__('pkg_resources').declare_namespace(__name__)
