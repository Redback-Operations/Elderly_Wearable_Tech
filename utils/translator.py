# utils/translator.py
import speech_recognition
import translate
import plotly
import pywaffle
import joblib

from translate import Translator


def get_translator(language_code):
    try:
        return Translator(to_lang=language_code)
    except Exception as e:
        print("Translation error:", e)
        return None

def translate_text(translator, text):
    try:
        return translator.translate(text)
    except:
        return text  # fallback if translation fails
