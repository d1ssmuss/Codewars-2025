import string


def rot13(message):
    """
    ROT13 - это простой шифр с подстановкой букв, который заменяет букву на 13 букв после нее в алфавите. ROT13 - это пример шифра Цезаря.

    Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13. Если в строку включены цифры или специальные символы, они должны быть возвращены в том виде, в каком они есть. Только буквы латинского/английского алфавита должны быть сдвинуты, как в оригинальной "реализации" Rot13.

    Пожалуйста, обратите внимание, что использование encode считается мошенничеством.
    :param message:
    :return:
    """
    letters = {string.ascii_lowercase[i]:i+1 for i in range(26)}
    # print(letters)
    big_letters = {string.ascii_uppercase[i]:i+1 for i in range(26)}
    nums_letters = {i + 1 : string.ascii_letters[i] for i in range(26)}
    big_nums_letters = {i + 1: string.ascii_uppercase[i] for i in range(26)}
    word = ''
    for i in message:
        if i not in letters.keys() and i not in big_letters.keys():
            word += i
        else:
            if i in string.ascii_uppercase:
                word += big_nums_letters[((big_letters[i] + 13 - 1) % 26) + 1]
            else:
                word += nums_letters[((letters[i] + 13 - 1) % 26) + 1]
    return word

