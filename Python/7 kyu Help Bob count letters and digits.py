def count_letters_and_digits(s):
    return len([i for i in s if i.isalpha() or i.isdigit()])
