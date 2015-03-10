#!/usr/bin/env python
import os
import sys
import schedule
import crashreports
import templates_builder
sys.path.append(os.path.dirname(__file__))


def application(environ, start_response):
    if environ['PATH_INFO'] == '/add':
        schedule.add(environ)
    if environ['PATH_INFO'] == '/remove':
        schedule.remove(environ)
    if environ['PATH_INFO'] == '/crash':
        crashreports.add(environ)
    if environ['PATH_INFO'] == '/table':
        content = "<p>This is my website that I made by myself!</p>"
        mapping = {
               'title': 'Welcome to my Website',
               'content': content,}
        return templates_builder.render('index.html', mapping)
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
