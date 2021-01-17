import requests
from pprint import pprint



TOKEN = ''  # please write your token


def create_folder(folder_name):
    HEADERS = {"Authorization": f'OAuth {TOKEN}'}
    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": folder_name},
        headers=HEADERS
    )
    print(response.status_code)
    pprint(response.json())
    return response.status_code

def folder_search(folder_name):
    HEADERS = {"Authorization": f'OAuth {TOKEN}'}
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": folder_name},
        headers=HEADERS
    )
    print(response.status_code)
    pprint(response.json())
    return response.status_code


if __name__ == '__main__':
    create_folder('folder')
    print()
    folder_search('folder')