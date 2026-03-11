

def to_camel_case(text):
    words = []
    word = ''
    flag = None
    for letter in text:
        if letter.isalpha():
            if flag:
                word += letter.upper()
                flag = False
            else:
                word += letter
            words.append(word)
            word = ''
        else:
            flag = True
    return ''.join(words)


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))

print(to_camel_case("The-Stealth_Warrior"))
