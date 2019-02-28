import re
from .http import http404, http405


class Router:
    def __init__(self):
        self.routes = []

    def add(self, method, path, callback):
        self.routes.append({
            'method': method,
            'path': path,
            'path_compiled': re.compile(path),
            'callback': callback
        })

    def match(self, method, path):
        error_callback = http404
        for r in self.routes:
            matched = r['path_compiled'].match(path)
            if not matched:
                continue

            error_callback = http405
            url_vars = matched.groupdict()
            if method == r['method']:
                return r['callback'], url_vars
        return error_callback, {}
