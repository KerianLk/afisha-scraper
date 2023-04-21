import requests


class Downloader:
    def __init__(self, url, params, method='GET'):
        self.url = url
        self.params = params
        self.method = method

    def get_html(self):
        req = requests.get(self.url, self.params)
        if req.status_code // 100 == 2:
            return req.text
        else:
            raise ValueError(f"Не удалось выполнить запрос. Код ошибки {req.status_code}")

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.get_html())
