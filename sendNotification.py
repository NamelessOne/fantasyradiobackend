#!/usr/bin/env python
__author__ = 'NamelessOne'
import pymysql
import consts
from datetime import datetime
import urllib.parse
import json
from urllib.request import Request, urlopen


def send_notification(user_keys):
    #-----------------------------
    url = 'https://android.googleapis.com/gcm/send'

    headers = {
        'Content-Type:application/json',
        'Authorization:key=' + consts.API_KEY
    }
    #-----------------------------
    json.dumps(user_keys)
    print(json)
    data = {'param1': 'value1', 'param2': 'value2'}
    details = urllib.parse.urlencode(data)
    #-----------------------------
    pass


def get_all_entities_before_datetime(time):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("SELECT CLIENT_KEY FROM ScheduleEntities WHERE TIME < %s", time)
    except pymysql.DataError as e:
        #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
        s = str(e.args[0])
    except pymysql.IntegrityError as e:
        s = str(e.args[0])
    except pymysql.ProgrammingError as e:
        s = str(e.args[0])
    except pymysql.NotSupportedError as e:
        s = str(e.args[0])
    #for key in cur:
    #    send_notification(key)
    send_notification(cur.fetchall())
    return s


def remove_all_entities_before_datetime(time):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM ScheduleEntities WHERE TIME < %s", time)
    except pymysql.DataError as e:
        #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
        s = str(e.args[0])
    except pymysql.IntegrityError as e:
        s = str(e.args[0])
    except pymysql.ProgrammingError as e:
        s = str(e.args[0])
    except pymysql.NotSupportedError as e:
        s = str(e.args[0])
    return s

#main
now = datetime.now()
print(now)
get_all_entities_before_datetime(now)
remove_all_entities_before_datetime(now)

