#!/usr/bin/env python
import os
import sys
import schedule
import crashreports
import templates_builder
import hashlib
from http.cookies import SimpleCookie
import urllib.parse

sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    if environ['PATH_INFO'] == '/add':
        schedule.add(environ)
    if environ['PATH_INFO'] == '/remove':
        schedule.remove(environ)
    if environ['PATH_INFO'] == '/crash':
        crashreports.add(environ)
    if environ['PATH_INFO'] == '/table':
        if is_authorized(environ):
            content = crashreports.build_reports_table()
            mapping = {'title': 'Welcome to my Website', 'content': content}
            start_response('200 OK', [('Content-Type', 'text/html')])
            return templates_builder.render('table.html', mapping)
        else:
            start_response('301 Redirect', [('Location', 'http://www.example.com/')])
            return ''
    if environ['PATH_INFO'] == '/auth':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return templates_builder.render('auth.html', 'text/html')
    if environ['PATH_INFO'] == '/login':
        environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()  # ip
        post_input = urllib.parse.parse_qs(environ['wsgi.input'].readline().decode(), True)
        m = hashlib.md5()
        m.update((environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip() + post_input['username'][0] +
                 post_input['password'][0]).encode('utf-8'))
        cookie = SimpleCookie()
        cookie['login'] = m.hexdigest()
        start_response('200 OK', [('Content-Type', 'text/html'), ('Set-Cookie', cookie['login'].OutputString())])
        return "OK"
        #return get_client_ip(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
    #Hello %(subject)s!
    ''' % {'subject': '111'}]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_reques()


def is_authorized(environ):
    if 'HTTP_COOKIE' in environ:
        cookie = SimpleCookie(environ['HTTP_COOKIE'])
        if 'login' in cookie:
            # handle the cookie value
            return cookie['login'].value == '111'
    pass