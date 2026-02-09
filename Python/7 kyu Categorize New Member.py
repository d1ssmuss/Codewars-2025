def open_or_senior(data):
    return ["Senior" if x >= 55 and y > 7 else "Open" for (x,y) in data]

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
print(open_or_senior([(67, 20), (81, 23), (66, 20), (73, 7), (63, 2)])) # ['Senior', 'Senior', 'Senior', 'Senior', 'Open'] should equal ['Senior', 'Senior', 'Senior', 'Open', 'Open']