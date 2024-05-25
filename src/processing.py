def changing_the_list(list_of_dict: list, state: str = "EXECUTED") -> list:
    """
    Функция, которая принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение
    """
    default_list_dictionary = []
    for state_key in list_of_dict:
        if state_key["state"] == state:
            default_list_dictionary.append(state_key)
    return default_list_dictionary
