def neutralise(s1, s2):
    new_s = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            new_s += s1[i]
        else:
            new_s += "0"
    return new_s


print(neutralise("-+-+-+", "-+-+-+"))