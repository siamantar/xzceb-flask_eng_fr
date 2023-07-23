import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_english_to_french_bonjour(self):
        result = english_to_french("Bonjour")
        self.assertEqual(result, "Bonjour")  # In English, "Bonjour" remains "Bonjour"

    def test_french_to_english_bonjour(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

    def test_french_to_english_hello(self):
        result = french_to_english("Hello")
        self.assertEqual(result, "Hello")  # In English, "Hello" remains "Hello"

if __name__ == "__main__":
    unittest.main()