import re

def sanitize_input(text):
    banned_words = ['kill', 'suicide', 'damn', 'hell']
    clean_text = re.sub(r'\b(?:' + '|'.join(banned_words) + r')\b', '[censored]', text, flags=re.IGNORECASE)
    return clean_text.strip()









