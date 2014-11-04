__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

import yaml
from copy import deepcopy as copy


class ConfigurationSection:
    def __init__(self, config=None, name=None, path=None):
        if config is None:
            self._config = {}
        elif type(config) is dict:
            self._config = config
        else:
            raise TypeError("Configuration must be a dictionary")
        self._name = name
        self._path = path

    def get_name(self):
        return self._path

    def get_path(self):
        return self._path

    def _get(self, path):
        path = path.split(".")
        node = self._config
        for key in path:
            node = node[key]
        return node

    def get(self, path, default=None):
        val = self._get(path)
        if type(val) is dict:
            name = path.rsplit('.', 1)[1]
            if self.get_path() is None:
                full_path = path
            else:
                full_path = self.get_path() + '.' + path
            return ConfigurationSection(val, name, full_path)
        else:
            return copy(val)

    def set(self, path, value):
        path = path.rsplit('.', 1)
        self.__get(path[0])[path[1]] = value

    def keys(self):
        return self._config.keys()

    def as_string(self):
        return str(self._config)

    def as_yaml(self):
        return yaml.dump(self._config)