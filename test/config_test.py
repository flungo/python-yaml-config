__author__ = 'Fabrizio Lungo<fab@lungo.co.uk>'

import unittest
import shutil
import os
from config import Configuration

testdir = './files'
testconfig = testdir + '/config.yml'
exampledir = '../examples/yaml'

class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        shutil.rmtree(testdir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(testdir)

    def setUp(self):
        shutil.rmtree(testdir)
        os.makedirs(testdir)

    def tearDown(self):
        shutil.rmtree(testdir)

    def test_create_config(self):
        conf = Configuration()


if __name__ == '__main__':
    unittest.main()