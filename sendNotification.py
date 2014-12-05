#!/usr/bin/env python
__author__ = 'NamelessOne'
import pymysql
import consts
from datetime import datetime, tzinfo
import urllib.parse
import json
from urllib.request import Request, urlopen
import urllib.error
import pytz


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


def send_notification(user_keys):
    #TODO отправлять не более тысячи за раз
    #-----------------------------
    url = 'https://android.googleapis.com/gcm/send'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + consts.API_KEY
    }

    #-----------------------------
    data = {'param1': 'value1', 'param2': 'value2'}
    json_body = {"registration_ids": user_keys, "data": data}
    #----------------------------
    r = Request(url=url, headers=headers, data=json.dumps(json_body).encode())
    try:
        urllib.request.urlopen(r)
    except urllib.error.HTTPError:
        print("httpError")
    return


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
tz_moscow = pytz.timezone('Europe/Moscow')
now = datetime.now(tz_moscow)
print(now)
get_all_entities_before_datetime(now)
remove_all_entities_before_datetime(now)

