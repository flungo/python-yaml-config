__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

import os

import yaml

from __exceptions__.FileNotFound import FileNotFound
from section import ConfigurationSection


class Configuration(ConfigurationSection):
    def __init__(self, fn='config.yml', name=None, create=False):
        self._fn = fn
        self._create = create
        self.reload()
        if name is None:
            name=fn
        self._name = name

    def reload(self):
        if self._create and not os.path.exists(self._fn):
            self._config = {}
        elif os.path.exists(self._fn):
            with open(self._fn, "r") as f:
                self._config = yaml.load(f)
        else:
            raise FileNotFound(filename=self._fn)

    def save(self):
        with open(self._fn, "w") as f:
            yaml.dump(self._config, f)