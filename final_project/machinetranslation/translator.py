"""
translator.py: A module that provides functions to translate text 
between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.

    Parameters:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translator = MyMemoryTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.

    Parameters:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translator = MyMemoryTranslator(source='french', target='english')
    english_text = translator.translate(french_text)
    return english_text