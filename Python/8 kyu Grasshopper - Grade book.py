def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    match score:
        case score if 90 <= score <= 100:
            return 'A'
        case score if 80 <= score < 90:
            return 'B'
        case score if 70 <= score < 80:
            return 'C'
        case score if 60 <= score < 70:
            return 'D'
        case score if 0 <= score < 60:
            return 'F'


# Из теста A
print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(92, 93, 94))
print(get_grade(100, 100, 100))

# Из теста B
print(get_grade(70, 70, 100))
print(get_grade(82, 85, 87))
print(get_grade(84, 79, 85))

# Из теста C
print(get_grade(70, 70, 70))
print(get_grade(75, 70, 79))
print(get_grade(60, 82, 76))

# Из теста D
print(get_grade(65, 70, 59))
print(get_grade(66, 62, 68))
print(get_grade(58, 62, 70))

# Из теста F
print(get_grade(44, 55, 52))
print(get_grade(48, 55, 52))
print(get_grade(58, 59, 60))
print(get_grade(0, 0, 0))