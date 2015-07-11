# -*- coding: utf-8 -*-
import pymysql
import consts
import json
import sys

if sys.version < '3':
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x


def get_schedule():
    objects_list = []
    rows = _get_db_entities()
    for row in rows:
        d = {'summary': row['summary'], 'description': row['description'], 'start': row['start'].isoformat(),
             'end': row['end'].isoformat(), 'img': row['img']}
        objects_list.append(d)
    print(json.dumps(objects_list, ensure_ascii=False))
    return repr(json.dumps(objects_list, ensure_ascii=False))


def _get_db_entities():
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                               use_unicode=True, charset='utf8')
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT summary, description, start, end, img FROM CalendarEvents')
        rows = cur.fetchall()
        # ------------------------
        return rows
    finally:
        cur.close()
        conn.close()
    pass