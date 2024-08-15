def get_mask_card_number(card_number: str):
    """Функция маскировки номера карты"""
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[:4]


def get_mask_account(account: str):
    """Функция маскировки счёта"""
    return "**" + account[:4]
