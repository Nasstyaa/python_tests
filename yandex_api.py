import requests
import json
from pprint import pprint

#url = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQAAAAAD23BEAAfQzDonw96jhUSlsa5I4-m7vFI'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path, url):

    res = requests.put(f'{url}?path={path}', headers=headers)
    print(res.status_code)
    return res.status_code

create_folder('new_folder', 'https://cloud-api.yandex.net/v1/disk/resources')



