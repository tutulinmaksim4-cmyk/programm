def get_mask_card_number(card_number: int) -> str:
    """ "Функция маскирует номер банковской карты"""
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """ "Функция которая принимает на вход номер счета и возвращает его маску формате
    **XXXX"""
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
