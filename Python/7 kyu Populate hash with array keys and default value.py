def populate_dict(keys, default):
    """
    Завершите работу функции так, чтобы она принимала набор ключей и значение по умолчанию и возвращала хэш (Ruby)
    / словарь (Python)
    / карту (Scala)
    со всеми ключами, установленными на значения по умолчанию.

    Пример
    populate_dict(["draft", "completed"], 0)  # should return {"draft": 0, "completed: 0}
    """
    return dict.fromkeys(keys, default)


print(populate_dict(["draft", "completed"], 0))