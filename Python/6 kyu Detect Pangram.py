def is_pangram(st):
    return True if len(set([i.lower() for i in st if i.isalpha()])) == 26 else False
