import unittest
import uuid
import cffi
import importlib

def load(filename):
    # generate random name
    name = filename + '_' + uuid.uuid4().hex
    
    with open(filename + '.c','r') as f :        
        source = f.read()
    with open(filename + '.h','r') as f :
        includes = f.read()
    

    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(name, source)
    ffibuilder.compile()
    
    module = importlib.import_module(name)
    return module.lib

class SumTest(unittest.TestCase):
    def setUp(self):
        self.module = load('sum')
        
    def test_zero(self):
        self.assertEqual(self.module.sum(0), 0)

    def test_one(self):
        self.assertEqual(self.module.sum(1), 1)

    def test_multiple(self):
        self.assertEqual(self.module.sum(2), 2)
        self.assertEqual(self.module.sum(4), 2 + 4)


if __name__ == "__main__":
 unittest.main()        