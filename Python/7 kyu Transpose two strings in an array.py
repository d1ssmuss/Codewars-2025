def transpose_two_strings(arr):
    """
    Вам будет предоставлен массив, содержащий две строки. Ваша задача - создать функцию,
    которая возьмет эти две строки и преобразует их таким образом, чтобы строки шли сверху вниз, а не слева направо.
    Например, транспонировать две строки(['Hello','World']);
    должно быть возвращено
    H W
    e o
    l r
    l l
    o d
    Несколько моментов, на которые следует обратить внимание:
    1. Между двумя символами должен быть один пробел
    2. Вам не нужно изменять регистр (т.е. не нужно менять на верхний или нижний)
    3. Если одна строка длиннее другой, то вместо символа должен быть пробел.
    :param arr:
    :return:
    """
    t = ""
    if len(arr[0]) > len(arr[1]):
        arr[1] += " " * (len(arr[0]) - len(arr[1]))
        for i in range(len(arr[0])):
            if i == len(arr[0]) - 1:
                t += arr[0][i] + " " + arr[1][i]
            else:
                t += arr[0][i] + " " + arr[1][i] + "\n"
    elif len(arr[0]) < len(arr[1]):
        arr[0] += " " * (len(arr[1]) - len(arr[0]))
        for i in range(len(arr[1])):
            if i == len(arr[1]) - 1:
                t += arr[0][i] + " " + arr[1][i]
            else:
                t += arr[0][i] + " " + arr[1][i] + "\n"
    else:
        for i in range(len(arr[1])):
            if i == len(arr[1]) - 1:
                t += arr[0][i] + " " + arr[1][i]
            else:
                t += arr[0][i] + " " + arr[1][i] + "\n"
    return t



t = ['Hello','World']
print(transpose_two_strings(t))
# print("H W\ne o\nl r\nl l\no d")
# print("j l\no o\ne u\ny i\n  s\n  e")