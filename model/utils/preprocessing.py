import re

def clean_text(text):
    text = text.lower()
    text = remove_extra_spaces(text)
    text = remove_special_symbols(text)
    return text

def remove_extra_spaces(text):
    return " ".join(text.split())

def remove_special_symbols(text):
    text = re.sub(r"[^a-zA-Z0-9\s.,?]", "", text)
    return text

def tokenize_text(text):
    return text.split()

def display_tokens(text):
    tokens = tokenize_text(text)
    print("Tokens:")
    for token in tokens:
        print("-", token)
