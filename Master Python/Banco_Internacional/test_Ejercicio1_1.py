import unittest
import Ejercicio1_1

class testEjercicio1_1 (unittest.TestCase):
    def test_NonConsecutive(self):
        self.assertEqual(Ejercicio1_1.NonConsecutive(1, 6), 6)
        
if __name__ == "__main__":
    unittest.main()