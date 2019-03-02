import os

from jinja2 import Environment, FileSystemLoader

from .router import Router
from .request import Request
from .response import TemplateResponse
from .utils import flatten


class App:
    def __init__(self):
        self.router = Router()
        templates = [os.path.join(os.path.abspath('.'), 'templates')]
        self.jinja2_environment = Environment(loader=FileSystemLoader(templates))

    def route(self, urls):
        for url in flatten(urls):
            self.router.add(*url.spec)

    def __call__(self, env, start_response):
        request = Request(env)
        callback, url_vars = self.router.match(request.path)

        response = callback(request, **url_vars)
        start_response(response.status_code, response.header_list)
        if isinstance(response, TemplateResponse):
            return [response.render_body(self.jinja2_environment)]
        return response.body
