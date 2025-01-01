"""
Вам предоставляется список направлений в виде списка:

цель = ["N", "S", "E", "W"]

Представьте, что каждое направление считается 1 шагом в этом конкретном направлении.

Ваша задача — создать функцию под названием «направления»,
которая будет возвращать сокращенный список, который приведет вас к той же точке.
Порядок направлений должен быть возвращен как N, затем S, затем E, затем W.

Если вы вернетесь к началу, верните пустой массив.
"""
def directions(goal):
    if goal.count("N") == goal.count("S") == goal.count("E") == goal.count("W"): # Если мы вернулись в начало(в начальную точку)
        return []
    else:
        """# словарь направлений
        directs = {
            "N": 0,
            "S": 0,
            "E": 0,
            "W": 0
        }
        # маршрут
        route = []
        str_route = ""
        for i in goal:
            if i in directs:
                directs[i] += 1"""
        route = []
        str_route = ""
        if goal.count("N") - goal.count("S") > 0:
            str_route += ("N" * (goal.count("N") - goal.count("S")))
        elif goal.count("N") - goal.count("S") < 0:
            str_route += ("S" * abs((goal.count("N") - goal.count("S"))))
        if goal.count("E") - goal.count("W") > 0:
            str_route += ("E" * (goal.count("E") - goal.count("W")))
        elif goal.count("E") - goal.count("W") < 0:
            str_route += ("W" * abs((goal.count("E") - goal.count("W"))))

        for i in str_route:
            route.append(i)
        return route




print(directions(["N","N","N","N","N","E","N","N"]))
print(directions(["S","S","N","E","W","S","N"]))
print(directions(["N","S","E","W"]))
