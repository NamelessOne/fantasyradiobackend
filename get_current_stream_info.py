import consts
import pymysql
import urllib.request
import html.parser


class CurrentStreamInfo:
    def __init__(self, stream_url, about):
        self.stream_url = stream_url
        self.about = about


def add_to_db(current_stream_info):
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                               use_unicode=True, charset='utf8')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute("INSERT INTO CurrentStreamInfo(ImageURL, About) VALUES "
                    "(%s, %s);", (current_stream_info.stream_url, current_stream_info.about))
        conn.commit()
    finally:
        cur.close()
        conn.close()
    pass

# MAIN
#response = urllib.request.urlopen(consts.STREAM_INFO_URL)
#test
add_to_db(CurrentStreamInfo("testscript", "testscript"))