def alphabet_position(text):
    return ' '.join([str(((ord(letter) - 1) % 96) + 1) for letter in text.lower() if letter.isalpha()])
