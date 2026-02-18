def first_non_repeating_letter(s):
    """
    Напишите функцию, которая принимает строковые входные данные и возвращает первый символ, который нигде в строке не повторяется.

    Например, если во входных данных указано "ударение", функция должна возвращать "t", поскольку буква t встречается в строке только один раз и является первой в строке.

    В качестве дополнительной проблемы, заглавные и строчные буквы считаются одним и тем же символом, но функция должна возвращать правильный регистр для начального символа. Например, при вводе "Ударение" должно возвращаться "T".

    Если строка содержит только повторяющиеся символы, верните пустую строку ("").;

    Примечание: несмотря на свое название на некоторых языках, ваша функция должна обрабатывать любую кодовую точку в Юникоде:
    :param s:
    :return:
    """
    s_l = s.lower()
    a = [i for i in s_l if s_l.count(i) == 1]
    if a:
        if a[0] not in s:
            return a[0].upper()
        else:
            return a[0]
    else:
        return ''


print(first_non_repeating_letter("abba"), '')
print(first_non_repeating_letter("aa"), '')
print(first_non_repeating_letter("Who is my widdle silly mopy doggy then?"), 'p')
print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('streSS'), 't')
print(first_non_repeating_letter('a'), 'a')
print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')
print(first_non_repeating_letter('@#@@*'), '#')
print(first_non_repeating_letter('かか何'), '何')
print(first_non_repeating_letter('🐐🦊🐐'), '🦊')
