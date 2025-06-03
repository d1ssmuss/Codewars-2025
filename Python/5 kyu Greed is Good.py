def score(dice):
    str_dice = [str(i) for i in dice]
    # _set = set(dice)
    score = 0
    for i in range(1, 7):
        max_i, dop_i = 0, 0
        max_i = str_dice.count(str(i))
        if max_i >= 3:
            max_i = 3
            dop_i = str_dice.count(str(i)) - max_i
            if i == 1:
                score += 1000 + (100 * dop_i)
            elif i == 5:
                score += (i * 100) + (dop_i * 50)
            else:
                score += (i * 100)
        else:
            if i == 1:
                score += 100 * max_i
            elif i == 5:
                score += 50 * max_i
    return score

print(score([5, 1, 3, 4, 1]))