import pytest
from yandex_api import TOKEN, headers, create_folder

@pytest.mark.parametrize(
    'x, y, expected', [
        ('new_folder', 'https://cloud-api.yandex.net/v1/disk/resources', 409),
        ('second_folder', 'https://cloud-api.yandex.net/v1/disk/resources', 201),
        ('third_folder', 'https://cloud-api.yandex.net/v1/disk', 405)

    ]
)
def test_yandex_api(x, y, expected):
    result = create_folder(x,y)
    assert result == expected



