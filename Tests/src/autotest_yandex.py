import requests


class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {"Authorization": f"OAuth {token}"}

    def create_folder(self, folder_path):
        params = {"path": folder_path}
        response = requests.put(self.base_url, headers=self.headers, params=params)
        return response

    def get_files_list(self):
        params = {"path": "/"}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        return response