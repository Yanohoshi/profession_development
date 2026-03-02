import pytest
import os
import time
from src.autotest_yandex import YandexDisk

TOKEN = os.environ.get("YANDEX_DISK_TOKEN")


@pytest.fixture
def disk():
    if not TOKEN:
        pytest.skip("Токен не найден. Установите YANDEX_DISK_TOKEN")
    return YandexDisk(TOKEN)


@pytest.fixture
def test_folder():
    return f"test_folder_{int(time.time())}"


def test_create_folder_success(disk, test_folder):
    response = disk.create_folder(test_folder)

    assert response.status_code == 201, f"Ожидался код 200, получен {response.status_code}"

    list_response = disk.get_files_list()
    assert list_response.status_code == 200, "Не удалось получить список файлов"

    items = list_response.json()["_embedded"]["items"]
    folder_names = [item["name"] for item in items]

    assert test_folder in folder_names, f"Папка {test_folder} не найдена в списке"
