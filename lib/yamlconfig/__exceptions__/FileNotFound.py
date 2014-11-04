__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

from exceptions import IOError

class FileNotFound(IOError):
    def __init__(self, msg=None, filename=None):
        if msg is None and type(filename) is str:
            msg = "The specified configuration file could not be found: " + filename;
        self.value = filename
        self._msg = msg
        self._filename = filename

    def __str__(self):
        return repr(self._msg);