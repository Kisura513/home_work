from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(payment_info: str, card_number: str) -> str:
    if payment_info == "Visa Platinum" or "Maestro":
        return get_mask_card_number(card_number)
    else:
        return get_mask_account(card_number)

def get_date(date: str) -> str:
