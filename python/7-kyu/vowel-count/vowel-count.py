def get_count(sentence):
    return sum(1 for letter in sentence.lower() if letter in "aeiou")