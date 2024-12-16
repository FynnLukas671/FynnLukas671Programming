import unittest

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(calculate_average([2, 4, 6, 8, 10]), 6)

    def test_negative_numbers(self):
        self.assertAlmostEqual(calculate_average([-1, -2, -3, -4]), -2.5)

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            calculate_average(["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()
