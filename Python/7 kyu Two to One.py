def longest(a1, a2):
    """Возьмем 2 строки s1 и s2, содержащие только буквы от a до z.
    Вернем новую отсортированную строку (в алфавитном порядке по возрастанию),
    как можно более длинную, содержащую отдельные буквы,
    каждая из которых берется только один раз, начиная с s1 или s2.

    Примеры:
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    longest(a, b) -> "abcdefklmopqwxy"

    a = "abcdefghijklmnopqrstuvwxyz"
    longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
    """
    t = list(dict.fromkeys(sorted(set(a1)) + sorted(set(a2))))
    t.sort()
    return "".join(t)

a = "abcdefghijklmnopqrstuvwxyz"
b = "xxxxyyyyabklmopq"
c = longest(a, a)
print(c == "abcdefghijklmnopqrstuvwxyz")