def to_jaden_case(text):
    text = " ".join([ word.capitalize() for word in text.split() ])
    return text