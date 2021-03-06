#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib
from http.cookies import SimpleCookie
import urllib.parse
import cgi

import crashreports
import templates_builder
import consts
import schedule
import sys
import current_stream

if sys.version < '3':
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    '''
    if environ['PATH_INFO'] == '/add':
        schedule.add(environ)
    if environ['PATH_INFO'] == '/remove':
        schedule.remove(environ)
    '''
    if environ['PATH_INFO'] == '/schedule':
        start_response('200 OK', [('Content-Type', 'application/json; charset=UTF-8')])
        return schedule.get_schedule()
    if environ['PATH_INFO'] == '/crash':
        crashreports.add(environ)
    if environ['PATH_INFO'] == '/table':
        if is_authorized(environ):
            content = crashreports.build_reports_table(cgi.parse_qs(environ.get('QUERY_STRING', '')))
            mapping = {'title': 'Welcome to my Website', 'content': content}
            start_response('200 OK', [('Content-Type', 'text/html')])
            return templates_builder.render('table.html', mapping)
        else:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return templates_builder.render('auth.html', 'text/html')
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
    if environ['PATH_INFO'] == '/delete':
        if is_authorized(environ):
            parameters = cgi.parse_qs(environ.get('QUERY_STRING', ''))
            if 'id' in parameters:
                crashreports.delete_report_by_id(cgi.escape(parameters['id'][0]))
            content = crashreports.build_reports_table()
            mapping = {'title': 'Welcome to my Website', 'content': content}
            start_response('200 OK', [('Content-Type', 'text/html')])
            return templates_builder.render('table.html', mapping)
        else:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return templates_builder.render('auth.html', 'text/html')
    if environ['PATH_INFO'] == '/current':
        start_response('200 OK', [('Content-Type', 'application/json')])
        return current_stream.get_current_stream_info_json()
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [('''Привет %(subject)s
    #Hello %(subject)s!
    ''' % {'subject': '111'}).encode()]

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
            m = hashlib.md5()
            m.update((environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip() + consts.ADMIN_USER +
                      consts.ADMIN_PASSWORD).encode('utf-8'))
            return cookie['login'].value == m.hexdigest()
    pass