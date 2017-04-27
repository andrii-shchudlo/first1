class Auth_filter(object):
    def __init__(self, app, req_usernames, req_pass):
        self.app = app
        self.req_usernames = req_usernames
        self.req_pass = req_pass

    def __call__(self, environ, start_response):
        environ['USER_NAME'] = "test"
        environ['USER_PASS'] = "test"

        print (self.req_usernames)
        print (environ)

        if  environ.get('USER_NAME') in self.req_usernames:
            if environ.get('USER_PASS') in self.req_pass:
                 return self.app(environ, start_response)
        start_response('403', [('Content-type', 'text/html')])
        return [' 403 You are forbidden to view this resource']
