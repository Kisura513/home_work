import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card, result_card", [("счет 12345678901234567890", "счет **7890"),
                                               ("Visa Super 1234567890123456", "Visa Super 1234 56** **** 3456"),
                                               ("счет 1234567890123456",
                                                "счет **3456")])
def test_widget_mask_card(card, result_card):
    assert mask_account_card(card) == result_card


@pytest.mark.parametrize("date, result_date", [("2019-07-03T18:35:29.512364", "03.07.2019"),
                                               ("2018-06-30T02:08:58.425572", "30.06.2018"),
                                               ("2018-09-12T21:27:25.241689", "12.09.2018"),
                                               ("21312534221", "22.53.2131")])
def test_widget_date(date, result_date):
    assert get_date(date) == result_date
