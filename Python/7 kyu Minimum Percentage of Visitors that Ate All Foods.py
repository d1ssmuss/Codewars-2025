def minimum_percentage(foods):
    return 100 - sum([100 - i for i in foods]) if (100 - sum([100 - i for i in foods])) > 0 else 0

print(minimum_percentage((97, 99, 94, 44, 65)))