import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b  
def es_par(a): return 1 if a%2 == 0 else 0

class PruebasFunciones(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba numeros")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def test_doblar(self):
        print("Realizando una prueba numeros2 ")
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        print("Realizando una prueba sumar")
        self.assertEqual(sumar(-15, 15), 0)
        self.assertEqual(sumar('Ab' ,'cd'), 'Abcd')

    def test_es_par(self):
        print("Realizando una prueba numeros pares")
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)

    def test_upper(self):
        print("Realizando una prueba mayus")
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        print("Realizando una prueba mayus 2")
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def test_split(self):
        print("Realizando una prueba split")
        s = 'Hola mundo'
        self.assertEqual(s.split(), ['Hola', 'mundo'])
        
    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)

if __name__ == '__main__':
    unittest.main()