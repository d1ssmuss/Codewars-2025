def is_vow(inp):
    for i in range(len(inp)):
        match inp[i]:
            case 97:
                inp[i] = 'a'
            case 101:
                inp[i] = 'e'
            case 105:
                inp[i] = 'i'
            case 111:
                inp[i] = 'o'
            case 117:
                inp[i] = 'u'

    return inp