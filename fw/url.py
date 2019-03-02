from .utils import flatten


class Url:
    def __init__(self, path, view):
        self.path = path
        self.view = view

    def union(self, path):
        self.path = path + self.path
        return self

    @property
    def spec(self):
        return self.path, self.view


def url(path, view=None, include=None):
    if view:
        return [Url(path, view)]
    if include:
        return [url_obj.union(path) for url_obj in flatten(include)]
