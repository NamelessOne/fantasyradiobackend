import pymysql
import consts


def clear_db():
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                               use_unicode=True, charset='utf8')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute("DELETE FROM CurrentStreamInformation WHERE id NOT IN (SELECT id FROM "
                    "(SELECT id FROM CurrentStreamInformation ORDER BY Created DESC LIMIT 120) foo);")
        conn.commit()
    finally:
        cur.close()
        conn.close()
    pass

# Main
clear_db()