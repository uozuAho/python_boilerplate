import unittest

from pboil.pack1.module_1 import Module1Thing

class Module1ThingTests(unittest.TestCase):
    def test_stuff(self):
        thing = Module1Thing()
        thing.run()
