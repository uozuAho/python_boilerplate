from .module_2 import Module2Thing

class Module1Thing:
    def run(self):
        thing = Module2Thing()
        print('module 1 thing calls module 2 thing.do_stuff:')
        thing.do_stuff()