import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """
    Test cases for the translator functions.
    """

    def test_english_to_french_translation(self):
        """
        Test English to French translation.
        """
        english_text = 'Hello'
        expected_french_text = 'Bonjour'
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_french_to_english_translation(self):
        """
        Test French to English translation.
        """
        french_text = 'Bonjour'
        expected_english_text = 'Hello'
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)


if __name__ == '__main__':
    unittest.main()
