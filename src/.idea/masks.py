def get_mask_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает маску."""

    s1 = number[:4] + " " + number[4:6] + "** **** " + number[-4:]
    return s1


number = input("Введите номер карты: ")

print(get_mask_card_number(number))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску."""

    s2 = "**" + account_number[-4:]
    return s2


account_number = input("Введите номер счета: ")

print(get_mask_account(account_number))