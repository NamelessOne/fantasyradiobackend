__author__ = 'NamelessOne'

# import consts
import urllib.request
import datetime
import json
import html.parser
import pymysql
import consts


class ScheduleCalendarEntity:
    def __init__(self, summary, description, start, end, img):
        self.summary = summary
        self.description = description
        self.start = start
        self.end = end
        self.img = img

    def get_mysql_end_time(self):
        res = str(self.end).replace('T', ' ')
        return res[:res.index('+')]

    def get_mysql_start_time(self):
        res = str(self.start).replace('T', ' ')
        return res[:res.index('+')]

    def __str__(self):
        return 'summary = ' + self.summary + ' description = ' + self.description + ' start = ' + self.start \
               + ' end = ' + self.end + ' img = ' + self.img


class ImageAndTextParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.img = ""
        self.text = ""
        self.td = False
        self.count = 0

    def handle_starttag(self, tag, attributes):
        if tag == 'img':
            attributes = dict(attributes)
            self.img = attributes['src']
        if tag == 'td':
            self.count += 1
            self.td = True

    def handle_endtag(self, tag):
        if tag == 'td':
            self.count = 0
            self.td = False
        pass

    def handle_data(self, data):
        if self.td:
            if len(data.strip()) > 0:
                self.text = data
        pass


def add_to_db(schedule_items):
    if len(schedule_items) == 0:
        return
    else:
        try:
            conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB,
                                   use_unicode=True, charset='utf8')
            cur = conn.cursor()
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute('SET character_set_connection=utf8;')
            cur.execute('DELETE FROM CalendarEvents;')
            for j in range(0, len(schedule_items)):
                cur.execute("INSERT INTO CalendarEvents(summary, description, start, end, img) VALUES "
                            "(%s, %s, %s, %s, %s);", (schedule_items[j].summary, schedule_items[j].description,
                                                      schedule_items[j].get_mysql_start_time(),
                                                      schedule_items[j].get_mysql_end_time(), schedule_items[j].img))

            conn.commit()
        finally:
            cur.close()
            conn.close()
        pass

# ---MAIN---
start_time = datetime.datetime.now() - datetime.timedelta(hours=-4)
end_time = start_time + datetime.timedelta(days=3)
response = urllib.request.urlopen(consts.CALENDAR_URL + '&timeMin=' + start_time.strftime('%Y-%m-%dT') +
                                  '00:00:00.000Z&timeMax='
                                  + end_time.strftime('%Y-%m-%dT') + '00:00:00.000Z')
s = str(response.read().decode('utf-8'))
json_obj = json.loads(s)
items = json_obj['items']
schedule_list = []
for i in range(0, len(items)):
    parser = ImageAndTextParser()
    raw_html = items[i]['description'].replace('ПОДРОБНЕЕ', '')
    parser.feed(raw_html)
    text = parser.text
    if text == '':
        text = raw_html
    schedule_list.append(ScheduleCalendarEntity(items[i]['summary'], text, items[i]['start']['dateTime'],
                                                items[i]['end']['dateTime'], parser.img))
# for entity in schedule_list:
#    print(entity.get_mysql_start_time())
add_to_db(schedule_list)
