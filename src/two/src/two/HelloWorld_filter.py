
class HelloWorld_filter(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        print (response_headers,status)

        return 'Hello world'


