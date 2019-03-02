import unittest

from fw import App
from fw.response import Response
from fw.url import url


def view(request):
    return Response('hello')


def view_name(request, name):
    return Response(f'hello {name}')


class AppTests(unittest.TestCase):

    def test_nested_urls(self):
        app = App()
        urls2 = [
            url('', view),
            url('/<name>', view_name),
        ]
        app.route([
            url('/', view),
            url('/user', include=urls2),
        ])
        self.assertListEqual(
            ['/', '/user', '/user/<name>'],
            app.router.urls,
        )
