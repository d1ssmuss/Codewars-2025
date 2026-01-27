def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        s = 0
        for i in range(begin_number, end_number+1, step):
            print(i)
            s += i
        return s


print(sequence_sum(2,6,2))