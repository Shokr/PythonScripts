import cgi

def notfound(environ, start_response):
    start_response('404 Not Found', [('content-type', 'text/plain')])
    return['404 Not Found']


class PathDispatcher:

    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'], environ = environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {k:params.getvalue(k) for k in params}
        handler = self.pathmap.get((method, path), notfound)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function

name_response = """
<html>
    <head>
        <title> Hello {name} </title>
    </head>
    <body>
        <h1>HELLO {name} </h1>
    </body>
</html>
"""

def name (environ, start_response):
    start_response('404 Not Found', [('content-type', 'text/plain')])
    params = environ['params']
    response = name_response.format(name=params.get('name'))
    yield response.encode('utf-8')

if __name__ == '__name__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher = register('GET', '/name', name)
    httpd = make_server('localhost', 8080, dispatcher)
    httpd.serve_forever()