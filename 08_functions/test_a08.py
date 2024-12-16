import unittest

def multiply(number1, number2=2):
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return number1 * number2

class TestMultiply(unittest.TestCase):
    def test_both_parameters(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_default_parameter(self):
        self.assertEqual(multiply(7), 14)

    def test_zero_multiplication(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply("text", 3)
        with self.assertRaises(TypeError):
            multiply(5, "text")

if __name__ == "__main__":
    unittest.main()
