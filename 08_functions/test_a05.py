import unittest

def to_uppercase(names):
    return list(map(lambda name: name.upper(), names))

def filter_names(names):
    return list(filter(lambda name: len(name) > 3, names))

class TestFunctionalProgramming(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase(["ana", "bob"]), ["ANA", "BOB"])

    def test_filter_names(self):
        self.assertEqual(filter_names(["Ana", "Bob", "Charlie", "Dave", "Eva"]), ["Charlie", "Dave"])

    def test_empty_list(self):
        self.assertEqual(to_uppercase([]), [])
        self.assertEqual(filter_names([]), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            to_uppercase(None)
        with self.assertRaises(TypeError):
            filter_names(123)

if __name__ == "__main__":
    unittest.main()
