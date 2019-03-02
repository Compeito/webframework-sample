import re
import unittest

from fw.response import Response
from fw.router import Router, route_to_regex
from fw.request import Request


def view(name):
    return Response(f'hello {name}')


class RouterTests(unittest.TestCase):

    def setUp(self):
        self.router = Router()
        self.router.add('/hoge/<fuga>', view)

    def test_route_to_tegex(self):
        test_paths = (
            ('/', '^/$'),
            ('/hoge/<fuga>', '^/hoge/(?P<fuga>\\w+)$'),
        )
        for a, b in test_paths:
            self.assertEqual(route_to_regex(a), re.compile(b))

    def test_url_vars(self):
        callback, url_vars = self.router.match('/hoge/foo')
        self.assertEqual(url_vars, {'fuga': 'foo'})

    def test_404_not_found(self):
        request = Request({})
        callback, url_vars = self.router.match('/fuga')
        response = callback(request)
        self.assertEqual(response.status, 404)
