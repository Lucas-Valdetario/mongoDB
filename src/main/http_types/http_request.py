class HttpRequest:
    def __init__(self, body: dict =None, headers=None, params=None) -> None:
        self.headers = headers
        self.body = body
        self.params = params