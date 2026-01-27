import string


def title_to_number(title):
    s = 0
    letters = {string.ascii_uppercase[i]:i+1 for i in range(26)}
    for i in range(len(title)):
        s += letters[title[::-1][i]] * (26 ** i)
    return s

print(title_to_number('A')) # 1
print(title_to_number('Z')) # 26
print(title_to_number('AA')) # 27
print(title_to_number('AZ')) # 52
print(title_to_number('BA'))
print(title_to_number('CODEWARS'))
print(title_to_number('ZZZTOP'))
print(title_to_number('OYAJI'))
print(title_to_number('LONELINESS'))
print(title_to_number('UNFORGIVABLE'))