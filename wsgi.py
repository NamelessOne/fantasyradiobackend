#!/usr/bin/env python
import os
import sys
import schedule
import crashreports
import templates_builder
from http.cookies import SimpleCookie
sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    if environ['PATH_INFO'] == '/add':
        schedule.add(environ)
    if environ['PATH_INFO'] == '/remove':
        schedule.remove(environ)
    if environ['PATH_INFO'] == '/crash':
        crashreports.add(environ)
    if environ['PATH_INFO'] == '/table':
        content = crashreports.build_reports_table()
        mapping = {'title': 'Welcome to my Website', 'content': content}
        start_response('200 OK', [('Content-Type', 'text/html')])
        return templates_builder.render('table.html', mapping)
    if environ['PATH_INFO'] == '/auth':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return templates_builder.render('auth.html', 'text/html')
    if environ['PATH_INFO'] == '/login':
        #TODO залогиниваемся
        environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
        start_response('200 OK', [('Content-Type', 'text/html')])
        return get_client_ip(environ)
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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip