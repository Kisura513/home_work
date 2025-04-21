import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("numbers, result", [("1234567890937561", "1234 56** **** 7561"),
                                             ("12345678901221321332", "**1332"),
                                             ("671438560713567013567134784391", 0)])
def test_masks(numbers, result):
    if len(numbers) == 16:
        assert get_mask_card_number(numbers) == result
    elif len(numbers) == 20:
        assert get_mask_account(numbers) == result
    else:
        return 0
