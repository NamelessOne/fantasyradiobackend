__author__ = 'NamelessOne'

import os
import pymysql
import CrashReport
from cgi import parse_qs, escape

host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
password = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
db = os.environ['OPENSHIFT_APP_NAME']

def add(self, environ):
    # Get data from fields
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    report = CrashReport(parameters)
    response_body = ""
    #TODO собственно тут парсим кучу параметров

    #Connect to base
    try:
        conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=db)
    except Exception as e:
        s = str(e)
        response_body += s
        return response_body
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO schedule(clientID,time) VALUES (%s,%s)", (report.clientid, report.time))
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