import unittest
import functionsA02Loesungen

# sum_value = 0
#
# def add_numbers(a, b):
#     global sum_value
#     sum_value += (a + b)
#     return sum_value

class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        global summe
        summe = 0

    def test_single_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_multiple_additions(self):
        add_numbers(4, 1)
        self.assertEqual(summe, 5)
        add_numbers(10, 5)
        self.assertEqual(summe, 20)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_numbers("a", 5)
        with self.assertRaises(TypeError):
            add_numbers(3, None)

if __name__ == "__main__":
    unittest.main()