"""
This module provides translation functions using the MyMemoryTranslator API.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.
    :param english_text: The English text to be translated.
    :return: The translated French text.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.
    :param french_text: The French text to be translated.
    :return: The translated English text.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text
