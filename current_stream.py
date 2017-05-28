import json
import pymysql
import consts


def get_current_stream_info_json():
    row = _get_db_entities()
    d = {'image_url': row['ImageURL'], 'about': row['About']}
    return json.dumps(d, ensure_ascii=False).encode('utf-8').decode('iso-8859-1')


def _get_db_entities():
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                               use_unicode=True, charset='utf8')
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT TOP 1 About, ImageURL FROM CurrentStreamInformation ORDER BY CREATED DESC LIMIT 1')
        row = cur.fetchall()
        # ------------------------
        return row
    finally:
        cur.close()
        conn.close()
    pass
