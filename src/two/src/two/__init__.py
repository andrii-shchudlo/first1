from pyramid.config import Configurator

import HelloWorld_filter
import Auth_filter

def main(global_conf, **settings):

    req_usernames = 'test'
    req_pass = 'test'
    req_usernames = req_usernames.split()

    def filter(app):
        return Auth_filter.Auth_filter(app, req_usernames, req_pass)

    def filter1(app):
        return HelloWorld_filter.HelloWorld_filter(app)

    return filter1





