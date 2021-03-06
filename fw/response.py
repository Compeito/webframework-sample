import os
import json
from http.client import responses as http_responses
from wsgiref.headers import Headers

from jinja2 import Environment, FileSystemLoader


class Response:
    default_status = 200
    default_charset = 'utf-8'
    default_content_type = 'text/html; charset=UTF-8'

    def __init__(self, body='', status=None, headers=None, charset=None):
        self._body = body
        self.status = status or self.default_status
        self.headers = Headers()
        self.charset = charset or self.default_charset

        if headers:
            for name, value in headers.items():
                self.headers.add_header(name, value)

    @property
    def status_code(self):
        return f'{self.status} {http_responses[self.status]}'

    @property
    def header_list(self):
        if 'Content-Type' not in self.headers:
            self.headers.add_header('Content-Type', self.default_content_type)
        return self.headers.items()

    @property
    def body(self):
        if isinstance(self._body, str):
            return [self._body.encode(self.charset)]
        return [self._body]


class JSONResponse(Response):
    default_content_type = 'text/json; charset=UTF-8'

    def __init__(self, dic, status=200, headers=None, charset=None, **dump_args):
        self.dic = dic
        self.json_dump_args = dump_args
        super().__init__('', status=status, headers=headers, charset=charset)

    @property
    def body(self):
        return [json.dumps(self.dic, **self.json_dump_args).encode(self.charset)]


def load_jinja2_env(templates=None):
    if templates is None:
        templates = [os.path.join(os.path.abspath('.'), 'templates')]
    return Environment(loader=FileSystemLoader(templates))


jinja2_env = load_jinja2_env()


class TemplateResponse(Response):
    default_content_type = 'text/html; charset=UTF-8'

    def __init__(self, filename, status=200, headers=None, charset='utf-8', **tpl_args):
        self.filename = filename
        self.tpl_args = tpl_args
        super().__init__(body='', status=status, headers=headers, charset=charset)

    @property
    def body(self):
        template = jinja2_env.get_template(self.filename)
        return [template.render(**self.tpl_args).encode(self.charset)]
