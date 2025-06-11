def validate_hello(greetings):
    greetings = greetings.lower()
    words = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for i in words:
        if i in greetings:
            return True
        else:
            continue
    else:
        return False



print(validate_hello("hallo asd"))