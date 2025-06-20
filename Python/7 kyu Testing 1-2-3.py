"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Ваша команда пишет новый текстовый редактор, и вы заинтересовались реализацией нумерации строк.

Напишите функцию, которая принимает список строк и возвращает перед каждой строкой правильный номер.

Нумерация начинается с 1. Формат - n: строка. Обратите внимание на двоеточие и пробел между ними.
"""

def number(lines):
    return [f"{i+1}: {lines[i]}" for i in range(len(lines))]


a = number(["a", "b", "c"])
print(a)
