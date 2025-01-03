def count_streets(streets, drivers):
    street_index = {street: index for index, street in enumerate(streets)}
    return [abs(street_index[drivers[i][0]] - street_index[drivers[i][1]]) - 1 for i in range(len(drivers))]

# Tests
"""
print(count_streets(["first", "second", "third", "fourth", "fifth", "sixth", "seven"],
                                         [("first", "second"), ("second", "seven"), ("sixth", "fourth")]))

print(count_streets(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
                                         [("j", "a"), ("b", "i"), ("c", "d"), ("e", "j"), ("i", "g"), ("a", "i"), ("f", "e"), ("a", "j"), ("e", "a"), ("e", "h"), ("h", "b")]))

print(count_streets(["Drive", "DrivE", "carefully"],
                                         [("Drive", "DrivE"), ("Drive", "carefully"), ("DrivE", "Drive"), ("Drive", "DrivE"), ("carefully", "Drive")]),)


print(count_streets(["first", "second"],[("second", "first")]))

"""

# Неправильное решение
"""
def count_streets(streets, drivers):
    distance_between_streets = [(abs(streets.index(drivers[i][0]) - streets.index(drivers[i][1])) - 1) for i in range(len(drivers))]
    return distance_between_streets
"""