from typing import Any


def filter_by_state(list_id: list, state) -> list[Any]:
    """ Функция фильтрации списка по значению state """
    state_new_list = []
    for info in list_id:
        for value in info.values():
            if value == state:
                state_new_list.append(info)
    return state_new_list


def sort_by_date(list_id: list) -> list[Any]:
    """ Функция сортировки списка по дате """
    sorted_list = sorted(list_id, key=lambda x: x['date'], reverse=True)
    return sorted_list
