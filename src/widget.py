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


print(mask_account_card('Счет 12345678901234567890'))
print(mask_account_card('Visa Super 1234567890123456'))
print(mask_account_card('Visa Super Puper Mega Big Card Name 1234567890123456'))
