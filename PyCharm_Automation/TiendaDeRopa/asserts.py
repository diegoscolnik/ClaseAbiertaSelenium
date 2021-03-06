import unittest


class PruebasDeStandars(unittest.TestCase):

    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 5 + 1
        b = 20
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a == b, 'a y b deberían ser iguales')

    def test_algo_mas_es_verdadero(self):
        self.assertTrue(2 + 2 == 3 + 1)

    def test_algo_es_falso(self):
        self.assertFalse(2 + 1 == 6, 'Esto debería ser falso')

    def test_algo_es_mayor(self):
        a = 5
        b = 3
        self.assertTrue(a > b)

    def test_algo_es_mayor_II(self):
         a = 5
         b = 3
         self.assertGreater(a, b)

    def test_algo_es_mayor_o_igual(self):
        a = 5
        b = 5
        self.assertGreaterEqual(a, b)

    def test_algo_es_menor(self):
        a = 5
        b = 8
        self.assertLess(a, b)

    def test_algo_es_menor_o_igual(self):
        a = 5
        b = 5
        self.assertLessEqual(a, b)

    def test_comparar_listas(self):
        a = [1, 2, 'Fruta']
        b = [1, 2, 'Fruta']
        self.assertListEqual(a, b)

    def test_compara_tuplas(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

    def test_compara_diccionarios(self):
        b = {'id': 1, 'nombre': 'Pepe', 'apellido': 'Suarez'}
        a = {'id': 1, 'nombre': 'Pepe', 'apellido': 'Suarez'}
        self.assertDictEqual(a, b)


if __name__ == '__main__':
    unittest.main()