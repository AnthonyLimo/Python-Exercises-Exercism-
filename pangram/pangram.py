import string

def is_pangram(sentence):
    sentence.lower()
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if not i in sentence.lower():
            return False
    return True