class Request:
    def __init__(self, environ):
        self.environ = environ
        self._body = None

    @property
    def path(self):
        return self.environ['PATH_INFO'] or '/'

    @property
    def method(self):
        return self.environ['REQUEST_METHOD'].upper()

    @property
    def body(self):
        if self._body is None:
            content_length = int(self.environ.get('CONTENT_LENGTH', 0))
            self._body = self.environ['wsgi.input'].read(content_length)
        return self._body
