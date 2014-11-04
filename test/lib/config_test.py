__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

import unittest
import shutil
import os
import sys

sys.path.append(os.path.realpath('../../lib/yamlconfig'))

from config import Configuration
from __exceptions__ import FileNotFound

testdir = './files'
testconfig = testdir + '/config.yml'
exampledir = '../examples/yaml'

class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(testdir):
            shutil.rmtree(testdir)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(testdir):
            shutil.rmtree(testdir)

    def setUp(self):
        if os.path.exists(testdir):
            shutil.rmtree(testdir)
        os.makedirs(testdir)

    def tearDown(self):
        if os.path.exists(testdir):
            shutil.rmtree(testdir)

    def test_create_config(self):
        """
        Tests creation of a blank configuration ensuring that the file is not created on the file system until after the
        save() method is called on the configuration object. Also implicitly tests writing blank config files.

        """
        conf = Configuration(testconfig, create=True)
        if os.path.exists(testconfig):
            self.fail("File should not be written until save() is executed")
        conf.save()
        self.assertTrue(os.path.isfile(testconfig), "File should exist after having been written")

    def test_config_doesnt_exist(self):
        """
        Tests trying to access a file that doesn't exist without setting the 'create' flag to True

        """
        try:
            Configuration(testconfig)
            self.fail("Loading configuration that does not exist should have raised an exception")
        except FileNotFound:
            pass # Do nothing

if __name__ == '__main__':
    unittest.main()