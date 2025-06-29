def row_sum_odd_numbers(number):
    n = 1
    sum = 0
    for i in range(number):
        sum += 1 + ((number) * (number - 1)) + 2 * i
    return sum
