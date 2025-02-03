def calc_poly(pol_list, x):
    """For
    6*x^3
    +
    3*x^2
    +
    5*x
    - 4
    with x = 4 the value is 448"""

    "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"


    rez = 0
    for i in range(1, len(pol_list) + 1):
        rez += (pol_list[i - 1] * (x ** (len(pol_list) - i)))

    s = "For "
    for i in range(1, len(pol_list) + 1):
        if (pol_list[i - 1] == 0):
            s += ""
        elif len(pol_list) - i == 1: # степень
            s += f"{abs(pol_list[i - 1])}*x"
        elif len(pol_list) - i == 0:
            if (pol_list[i - 1] < 0):
                s += f" - {abs(pol_list[i - 1])}"
            else:
                s += f" + {abs(pol_list[i - 1])}"
        else:
            if (pol_list[i - 1] < 0) and (len(pol_list) - i != 1) and (len(pol_list) - i != 0):
                s += f"- {abs(pol_list[i - 1])}*x^{len(pol_list) - i}"

            elif (pol_list[i - 1] > 0) and (len(pol_list) - i != 1) and (len(pol_list) - i != 0):
                s += f"{abs(pol_list[i - 1])}*x^{len(pol_list) - i}"
                s += " + "
    s += f" with x = {x} the value is {rez}"
    return s

print(calc_poly([2, 0, 5, -6, 4, 0], 2))
print(calc_poly([-1, -6, 28, 79], 35))
