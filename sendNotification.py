#!/usr/bin/env python
__author__ = 'NamelessOne'
import pymysql
import consts
import gcm
from datetime import datetime


def send_notification(user_key):
    gcm_object = gcm.GCM(consts.API_KEY)
    data = {'param1': 'value1', 'param2': 'value2'}
    gcm_object.json_request(registration_ids=user_key, data=data)
    pass


def get_all_entities_before_datetime(time):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("SELECT CLIENT_KEY FROM ScheduleEntities WHERE date < %s", time)
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
    send_notification(cur)
    return s


def remove_all_entities_before_datetime(time):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM ScheduleEntities WHERE date < %s", time)
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
f = open('1.txt', 'w')
f.write(now)
get_all_entities_before_datetime(now)
remove_all_entities_before_datetime(now)

