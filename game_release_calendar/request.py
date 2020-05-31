from urllib import request


class Request:
    def __init__(self, url):
        self.url = url


class Client:
    def __init__(self, req):
        self.req = req

    def get(self):
        source = request.urlopen(self.req.url)
        data = source.read()

        return data