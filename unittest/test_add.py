#! python3
import unittest
import cffi
import importlib

def load(filename):
    # load source code
    with open(filename + '.c', 'r') as f:
        source = f.read()
    with open(filename + '.h', 'r') as f:
        includes = f.read()    
    # source = open(filename + '.c','r').read()
    # includes = open(filename + '.h','r').read()
    
    # pass source code to CFFI
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(filename + '_', source)
    ffibuilder.compile()
    
    # import and return resulting module
    module = importlib.import_module(filename + '_')
    return module.lib
    
class AddTest(unittest.TestCase):
    
    def test_addition(self):

        module = load('add')

        self.assertEqual(module.add(1,2),1+2)

    




# run(AddTest)


if __name__ == "__main__":
 unittest.main()

# test_addition(__main__.AddTest)
