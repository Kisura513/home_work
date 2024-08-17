from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(payment_info: str) -> str:
    """ Функция маскировки номера счетов """
    if payment_info[:13] == "Visa Platinum":
        return payment_info[:13] + " " + get_mask_card_number(payment_info[14:])
    elif payment_info[:7] == "Maestro":
        return payment_info[:7] + " " + get_mask_card_number(payment_info[8:])
    else:
        return payment_info[:4] + " " + get_mask_account(payment_info[5:])


def get_date(date: str) -> str:
    """ Функция записи коректной даты """
    return date[8:10] + "." + date[5:7] + "." + date[:4]

