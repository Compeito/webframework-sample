import unittest
from fw.response import Response, JSONResponse, TemplateResponse


class ResponseTests(unittest.TestCase):

    def test_response(self):
        response = Response('hello')
        self.assertEqual(response.body, [b'hello'])

    def test_json_response(self):
        response = JSONResponse({'message': 'hello'})
        self.assertEqual(response.body, [b'{"message": "hello"}'])

    def test_template_response(self):
        response = TemplateResponse('test.html', name='world')
        self.assertEqual(response.body, [b'hello world'])
