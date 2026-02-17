class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i in list(set(integer_list) - set(values_list))]


print(List().remove_([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]))