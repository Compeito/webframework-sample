from .router import Router
from .request import Request
from .utils import flatten


class App:
    def __init__(self):
        self.router = Router()

    def route(self, urls):
        for url in flatten(urls):
            self.router.add(*url.spec)

    def __call__(self, env, start_response):
        request = Request(env)
        callback, url_vars = self.router.match(request.path)

        response = callback(request, **url_vars)
        start_response(response.status_code, response.header_list)
        return response.body
