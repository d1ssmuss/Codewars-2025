def is_int_array(arr):
    """
    Напишите функцию, которая:
        возвращает значение true, если каждый элемент в массиве является целым числом или числом с плавающей точкой без десятичных знаков.
        возвращает значение true, если массив пуст.
        возвращает значение false для всех остальных входных данных.
    :param arr:
    :return:
    """
    if type(arr) != list:
        return False
    else:
        for i in arr:
            if (type(i) == int or type(i) == float) and (int(i) == i):
                continue
            else:
                return False
        return True

print(is_int_array([]))
print(is_int_array([1,2,3,4]))
print(is_int_array([-11, -12, -13, -14]))
print(is_int_array([1.0, 2.0, 3.0]))
print(is_int_array([1, 2, None]))
print("1", is_int_array(True))