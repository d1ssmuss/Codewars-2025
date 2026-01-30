def bouncing_ball(h, bounce, window):
    result = 1
    if h > 0 and (0 < bounce < 1) and window < h:
        h *= bounce
        while h > window:
            # print(h)
            h *= bounce
            result += 2
    else:
        return -1
    return result


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))
