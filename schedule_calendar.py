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
            if self.count == 1:
                self.text = data
        pass


def add_to_db(schedule_items):
    if len(schedule_items) == 0:
        return
    else:
        try:
            conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
            cur = conn.cursor()
            cur.execute('DELETE FROM CalendarEvents')
            for i in range(0, len(schedule_items)):
                cur.execute("INSERT INTO CalendarEvents(summary, description, start, end, img) VALUES "
                            "(%s, %s, %s, %s, %s)", (schedule_items[i].summary, schedule_items[i].description,
                                                     schedule_items[i].get_mysql_start_time,
                                                     schedule_items[i].get_mysql_end_time, schedule_items[i].img))

            conn.commit()
        finally:
            cur.close()
            conn.close()
        pass

# ---MAIN---
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(days=3)
response = urllib.request.urlopen(consts.CALENDAR_URL + '&timeMin=' + start_time.strftime('%Y-%m-%dT') +
                                  '00:00:00.000Z&timeMax='
                                  + end_time.strftime('%Y-%m-%dT') + '00:00:00.000Z')
s = str(response.read().decode('utf-8'))
jsobj = json.loads(s)
items = jsobj['items']
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
# add_to_db(schedule_list)
