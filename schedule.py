#!/usr/bin/env python
import os
import pymysql
from cgi import parse_qs, escape

#parameters = parse_qs(environ.get('QUERY_STRING', ''))
#if 'subject' in parameters:
host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
password = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
db = os.environ['OPENSHIFT_APP_NAME']


def add(self, environ):
    # Get data from fields
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    response_body = ""
    if 'clientID' in parameters:
        clienID = escape(parameters['clientID'][0])
    if 'time' in parameters:
        time = escape(parameters['time'][0])
    #Connect to base
    try:
        conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=db)
    except Exception as e:
        s = str(e)
        response_body += s
    cur = conn.cursor()
    return ""


def remove(self, environ):
    return ""