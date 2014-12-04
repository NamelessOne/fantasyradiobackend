#!/usr/bin/env python
__author__ = 'NamelessOne'
import pymysql
import consts


def send_notification(userKey):
    pass


def get_all_entities_before_datetime(datetime):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("SELECT CLIENT_KEY FROM ScheduleEntities WHERE date < %s", datetime)
    except pymysql.DataError as e:
        #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
        s = str(e.args[0])
    except pymysql.IntegrityError as e:
        s = str(e.args[0])
    except pymysql.ProgrammingError as e:
        s = str(e.args[0])
    except pymysql.NotSupportedError as e:
        s = str(e.args[0])
    for key in cur:
        send_notification(key)
    return s


def remove_all_entities_before_datetime(datetime):
    s = ""
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM ScheduleEntities WHERE date < %s", datetime)
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