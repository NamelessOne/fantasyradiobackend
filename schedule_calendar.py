__author__ = 'NamelessOne'

# import consts
import urllib.request
import datetime
import json
import html.parser


class ScheduleCalendarEntity:
    def __init__(self, summary, description, start, end, img):
        self.summary = summary
        self.description = description
        self.start = start
        self.end = end
        self.img = img


class ImageAndTextParser(html.parser.HTMLParser):
    # TODO ???????? ?????????
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.img = ""
        self.text = ""

    def handle_starttag(self, tag, attributes):
        if tag == 'img':
            attributes = dict(attributes)
            self.img = attributes['src']
        if tag == 'td':
            if len(attributes) > 0:
                self.text += attributes[len(attributes) - 1]

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

# ---MAIN---
start = datetime.datetime.now()
end = start + datetime.timedelta(days=3)
response = urllib.request.urlopen("https://www.googleapis.com/calendar/v3/calendars/fantasyradioru@gmail.com/events?"
                                  "key=AIzaSyDam413Hzm4l8GOEEg-NF8w8wdAbUsKEjM&maxResults=50&singleEvents=true&"
                                  "orderBy=startTime&timeMin=" + start.strftime('%Y-%m-%dT') + '00:00:00.000Z&timeMax='
                                  + end.strftime('%Y-%m-%dT') + '00:00:00.000Z')
s = str(response.read().decode('utf-8'))
jsobj = json.loads(s)
items = jsobj['items']
for i in range(0, len(items)):
    parser = ImageAndTextParser()
    raw_html = items[i]['description'].replace('?????????', '')
    parser.feed(raw_html)
    description = parser.text
    if description == '':
        description = raw_html
    ScheduleCalendarEntity(items[i]['summary'], description, items[i]['start']['dateTime'],
                           items[i]['end']['dateTime'], parser.img)
