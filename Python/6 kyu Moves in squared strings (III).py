"""
a b c d
e f g h
i j k l
m n o p
diag_1_sym(s) =>
a e i m
b f j n
c g k o
d h l p

rotate
m i e a
n j f b
o k g c
p l h d



a b c d
e f g h
i j k l
m n o p


selfie_and_diag1(s)

abcd|aeim
efgh|bfjn
ijkl|cgko
mnop|dhlp i строка j стобец

"""
def rot_90_clock(strng):
    words = [] # words = [word1, word2, word3...]
    words = strng.split("\n")

    # беру первые символы и переворачиваю их
    # также между словами должны быть \n
    answ = []
    row = ""
    # во всех словах длина == (одинакова)
    for i in range(len(words[0])): # слова
        for j in range(len(words)): # буква
            row += words[j][i]
        row = row[::-1]
        answ.append(row)
        row = ""
    return "\n".join(answ)


def diag_1_sym(strng):
    words = []  # words = [word1, word2, word3...]
    words = strng.split("\n")

    # беру первые символы и переворачиваю их
    # также между словами должны быть \n
    answ = []
    row = ""
    # во всех словах длина == (одинакова)
    for i in range(len(words[0])):  # слова
        for j in range(len(words)):  # буква
            row += words[j][i]
        answ.append(row)
        row = ""
    return "\n".join(answ)

def selfie_and_diag1(strng):
    words = []  # words = [word1, word2, word3...]
    words = strng.split("\n")

    # беру первые символы и переворачиваю их
    # также между словами должны быть \n
    answ = []
    row = ""
    # во всех словах длина == (одинакова)
    for i in range(len(words[0])):  # слова
        row = words[i] + "|" # первое слово
        for j in range(len(words)):  # буква
            row += words[j][i]
        answ.append(row)
        row = ""
    return "\n".join(answ)

def oper(fct, s):
    return fct(s)


print(oper(selfie_and_diag1, "abcd\nefgh\nijkl\nmnop"))
