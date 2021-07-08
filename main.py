import requests
import os

file = 'test.txt'
file_path = os.path.join(os.getcwd(), file)

token = TOKEN

class YaUploader:
    def __init__(self, token, file_path):
        self.token = token
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, file_path, disk_file_path):
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return f'Файл "{file}" загружен'

if __name__ == '__main__':
    ya = YaUploader(token, file_path)
    print(ya.upload_file(file_path, disk_file_path = "python/test.txt"))