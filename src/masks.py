def get_mask_card_number(number: str) -> str:
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(account_number: str) -> str:
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    card_input = input("Введите номер карты: ")
    print(get_mask_card_number(card_input))

    account_input = input("Введите номер счета: ")
    print(get_mask_account(account_input))
