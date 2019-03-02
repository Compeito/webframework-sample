import unittest

from fw import App
from fw.response import Response
from fw.url import url


def view():
    return Response('hello')


def view_name(name):
    return Response(f'hello {name}')


urls2 = [
    url('/', view),
    url('/<name>', view_name),
]

urls = [
    url('/', view),
    url('/user', include=urls2),
]


class AppTests(unittest.TestCase):

    def test_nested_urls(self):
        app = App()
        app.route(urls)
        self.assertListEqual(
            ['/', '/user/', '/user/<name>'],
            app.router.urls,
        )
