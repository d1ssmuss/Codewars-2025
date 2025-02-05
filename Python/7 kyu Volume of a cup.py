import math
def cup_volume(d1, d2, height):
    return round((1/3) * math.pi * height * ((d1/2)**2 + (d1/2)*(d2/2) + (d2/2)**2), 2)


print(cup_volume(1000,1000,1000))