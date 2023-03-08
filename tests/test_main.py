from unittest import TestCase
from main import get_visits, geo_logs, ids, unique_ids, get_unique_values, stats, get_key_with_max_value

def test_get_visits():
    result = get_visits(geo_logs)
    for i in result:
        assert 'visit1' in i or 'visit3' in i or 'visit7' in i or 'visit8' in i or 'visit9' in i or 'visit10' in i

def test_unique_ids():
    result = get_unique_values(ids, unique_ids)
    assert [213, 15, 54, 119, 98, 35] == result


def test_get_key_with_max_value():
    result = get_key_with_max_value(stats)
    assert 'yandex' == result



