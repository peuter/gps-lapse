# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.
import logging
import logging.config
import os
import configparser
import re
from io import StringIO


class Environment:
    """
    The global information container, used as a singleton.
    """
    # externally set as class variable
    config_dir = None

    config = None
    log = None
    __instance = None

    def __init__(self):
        self.log = logging.getLogger(__name__)

        # Load configuration
        self.__load_config(Environment.config_dir)

    def __get_cfg_files(self, cdir):
        conf = re.compile(r"^[a-z0-9_.-]+\.conf$", re.IGNORECASE)
        try:
            return [os.path.join(cdir, cfile)
                    for cfile in os.listdir(cdir)
                    if os.path.isfile(os.path.join(cdir, cfile)) and conf.match(cfile)]
        except OSError:
            return []

    def __load_config(self, config_dir):
        config_files = self.__get_cfg_files(config_dir)
        config_files.insert(0, os.path.join(config_dir, "config"))

        self.config = configparser.RawConfigParser()
        files_read = self.config.read(config_files)
        if not files_read:
            self.log.warning("no config files found in path '%s', using default settings" % config_dir)
        else:
            self.__config_logging()

    def __config_logging(self):
        try:
            tmp = StringIO()
            self.config.write(tmp)
            tmp2 = StringIO(tmp.getvalue())
            logging.config.fileConfig(tmp2)
        except configparser.NoSectionError:
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(name)s - %(message)s')

    @staticmethod
    def getInstance():
        """
        Act like a singleton and return the
        :class:`gpsl.env.Environment` instance.
        ``Return``: :class:`gpsl.env.Environment`
        """
        if not Environment.__instance:
            Environment.__instance = Environment()
        return Environment.__instance