import os

from fw import App
from fw.response import Response, JSONResponse, TemplateResponse
from fw.static import StaticMiddleware
from fw.url import url

BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'statics')]

app = App()


def hello(request):
    return JSONResponse({'message': 'Hello World'})


def users(request):
    users_list = [f'user{i}' for i in range(10)]
    return TemplateResponse('users.html', title='User List', users=users_list)


def user_detail(request, name):
    return Response('Hello {name}'.format(name=name))


user_urls = [
    url('', users),
    url('/<name>', user_detail)
]

urls = [
    url('/', hello),
    url('/users', include=user_urls)
]

if __name__ == '__main__':
    app.route(urls)
    app = StaticMiddleware(app, static_root='statics', static_dirs=STATIC_DIRS)
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, app)
    httpd.serve_forever()
