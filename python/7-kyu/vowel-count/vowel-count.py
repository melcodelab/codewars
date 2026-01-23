def get_count(sentence: str) -> int:
    "Receives a phrase or sentence and returns the number of vowels it contains."
    return sum(1 for letter in sentence.lower() if letter in "aeiou")