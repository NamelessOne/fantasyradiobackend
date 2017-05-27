import consts
import pymysql
import urllib.request
import html.parser


class CurrentStreamInfo:
    def __init__(self, image_url, about):
        self.image_url = image_url
        self.about = about


class ImageParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.img = ""

    def handle_starttag(self, tag, attributes):
        if tag == 'img':
            attributes = dict(attributes)
            if 'alt' in attributes and attributes['alt'] == 'Страница автора':
                self.img = attributes['src']

#Третий tr, внутри него b
class AboutParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.about = ""
        self.trcount = 0
        self.b = False

    def handle_starttag(self, tag, attributes):
        if tag == 'tr':
            self.trcount += 1
        if tag == 'b' and self.trcount == 3:
            self.b = True

    def handle_endtag(self, tag):
        if tag == 'b':
            self.b = False

    def handle_data(self, data):
        if self.b:
            self.about = data


def add_to_db(current_stream_info):
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                               use_unicode=True, charset='utf8')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute("INSERT INTO CurrentStreamInformation(ImageURL, About) VALUES "
                    "(%s, %s);", (current_stream_info.image_url, current_stream_info.about))
        conn.commit()
    finally:
        cur.close()
        conn.close()
    pass

# MAIN
# Image
image_response = urllib.request.urlopen(consts.STREAM_INFO_PLAYER_URL)
image_html = str(image_response.read().decode('windows-1251'))
image_parser = ImageParser()
image_parser.feed(image_html)
#About
about_response = urllib.request.urlopen(consts.STREAM_INFO_ABOUT_URL)
about_html = str(about_response.read().decode('windows-1251'))
about_parser = AboutParser()
about_parser.feed(about_html)

stream_info = CurrentStreamInfo(image_parser.img, about_parser.about)
add_to_db(stream_info)