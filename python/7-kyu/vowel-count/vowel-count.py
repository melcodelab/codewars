def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    return len([letter for letter in sentence.lower() if letter in vowels])