def scramble(strng, array):
    s = ''
    d = {array[i]:strng[i] for i in range(len(array))}
    # print(d.items())
    for k,v in sorted(d.items()):
        s += v
    return s

print(scramble('abcd', [0, 3, 1, 2]))
