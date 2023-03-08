
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

new_list = []


def get_visits(geo_logs):
    for i in geo_logs:
        for value in i.values():
            if value[1] == 'Россия':
                new_list.append(i)

    return new_list



get_visits(geo_logs)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_ids = []
def get_unique_values(ids, unique_ids):
    for value in ids.values():
        for i in value:
            if i not in unique_ids:
              unique_ids.append(i)
            else:
                continue
    return unique_ids

get_unique_values(ids, unique_ids)

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def get_key_with_max_value(stats):
    m = max(stats, key=stats.get)
    return m

get_key_with_max_value(stats)