from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(payment_info: str) -> str:
    """ Функция маскировки номера счетов """
    name_card = ""
    card_account = ""
    parts = payment_info.split()
    for letter in parts:
        if letter.isalpha():
            name_card += letter
    for number in parts:
        if number.isdigit():
            card_account += number
    if parts[0].lower() == 'счет':
        return payment_info[:4] + " " + get_mask_account(card_account)
    elif len(card_account) == 16:
        return payment_info[:-17] + " " + get_mask_card_number(card_account)


def get_date(date: str) -> str:
    """ Функция записи коректной даты """
    return date[8:10] + "." + date[5:7] + "." + date[:4]
print(get_date("2018-10-14T08:21:33.419441"))