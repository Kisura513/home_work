from typing import List, Any


def filter_by_state(list_id: list, state="EXECUTED") -> list[Any]:
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


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                   ))

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                      ))
