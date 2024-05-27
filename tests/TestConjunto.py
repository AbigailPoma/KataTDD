import unittest
from src.logica.Conjunto import Conjunto
class TestConjunto(unittest.TestCase):
    def test_conjunto_vacioretornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

if __name__ == '__main__':
    unittest.main