import unittest,uuid
import subprocess,cffi,importlib

def load(filename):
    name = filename + '_' + uuid.uuid4().hex

    with open(filename + '.c','r') as f:
        source = f.read()
    # handle preprocessor directives
    with open(filename + '.h','r') as f:       

        includes = preprocess(f.read())
    
    ffibuilder = cffi.FFI()
    ffibuilder.cdef(includes)
    ffibuilder.set_source(name, source)
    ffibuilder.compile()
    
    module = importlib.import_module(name)
    return module.lib

def preprocess(source):
    return subprocess.run(['gcc', '-E', '-P', '-'],
                          input=source, stdout=subprocess.PIPE,
                          universal_newlines=True, check=True).stdout

class ComplexTest(unittest.TestCase):
    def setUp(self):
        self.module = load('complex')
        
    def test_addition(self):
        result = self.module.add([0, 1], [2, 3])
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imaginary, 4)



if __name__ == "__main__":
 unittest.main()                