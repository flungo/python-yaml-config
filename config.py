__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

import yaml
from section import ConfigurationSection


class Configuration(ConfigurationSection):
    def __init__(self, fn='config.yml', name=None):
        self.fn = fn
        self.reload()
        if name is None:
            name=fn
        self._name = name

    def reload(self):
        with open(self.fn, "r") as f:
            self._config = yaml.load(f)

    def save(self):
        with open(self.fn, "w") as f:
            yaml.dump(self._config, f)