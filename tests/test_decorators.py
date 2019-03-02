import unittest

from fw import App
from fw.decorators import require_GET, require_POST
from fw.response import Response
from fw.request import Request
from fw.url import url


@require_GET
def get_view(request):
    return Response('hello')


@require_POST
def post_view(request):
    return Response('hello')


class DecoratorsTest(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.app.route([
            url('/get', get_view),
            url('/post', post_view),
        ])

    def test_require_get_405(self):
        request = Request({'REQUEST_METHOD': 'POST'})
        callback, url_vars = self.app.router.match('/get')
        response = callback(request)
        self.assertEqual(response.status, 405)

    def test_require_post_200(self):
        request = Request({'REQUEST_METHOD': 'POST'})
        callback, url_vars = self.app.router.match('/post')
        response = callback(request)
        self.assertEqual(response.status, 200)
