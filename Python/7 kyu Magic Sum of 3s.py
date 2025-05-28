def magic_sum(arr):
    """
    The magic sum of 3s is calculated on an array by summing up odd numbers which include the digit 3.

    Complete the function which accepts an array of integers and returns its magic sum of 3s.

    Example: [3, 12, 5, 8, 30, 13] results in 16 (3 + 13)

    If there is no such number in the array, 0 should be returned.

    Магическая сумма в 3 секунды вычисляется для массива путем суммирования нечетных чисел, содержащих цифру 3.

    Выполните функцию, которая принимает массив целых чисел и возвращает магическую сумму в 3 секунды.

    Пример: [3, 12, 5, 8, 30, 13] в результате получается 16 (3 + 13)

    Если такого числа в массиве нет, то должно быть возвращено 0.

    :param arr:
    :return:
    """
    return sum([i for i in arr if i % 2 != 0 and '3' in str(i)])

# Tests
# print(magic_sum([30, 34, 330]))
