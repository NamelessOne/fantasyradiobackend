#!/usr/bin/env python
import pymysql
import cgi
import consts

#parameters = parse_qs(environ.get('QUERY_STRING', ''))
#if 'subject' in parameters:


def add(environ):
    # Get data from fields
    parameters = cgi.parse_qs(environ.get('QUERY_STRING', ''))
    response_body = ""
    if 'clientID' in parameters:
        client_key = cgi.escape(parameters['clientID'][0])
    if 'time' in parameters:
        time = cgi.escape(parameters['time'][0])
        #TODO time нужно отформатировать
    #Connect to base
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
        response_body += s
        return response_body
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO ScheduleEntities(CLIENT_KEY, TIME) VALUES (%s,%s)", (client_key, time))
    except pymysql.DataError as e:
        #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.IntegrityError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.ProgrammingError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.NotSupportedError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    conn.commit()
    cur.close()
    conn.close()
    return response_body


def remove(environ):
    return ""