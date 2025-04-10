import string 
string.punctuation

def remove_punctuation_and_lower(text: str):
    punctuation_free = "".join([i for i in text if i not in string.punctuation])
    lower = punctuation_free.lower()
    return lower