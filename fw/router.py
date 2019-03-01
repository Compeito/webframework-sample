import re
from .http import http404, http405


def route_to_regex(path: str):
    matched = re.findall('<\\w+>', path)
    re_path = path
    for pattern in matched:
        re_path = re_path.replace(pattern, f'(?P{pattern}\\w+)')
    return re.compile(f'^{re_path}$')


class Router:
    def __init__(self):
        self.routes = []

    def add(self, method, path, callback):
        self.routes.append({
            'method': method,
            'path': path,
            'path_compiled': route_to_regex(path),
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
