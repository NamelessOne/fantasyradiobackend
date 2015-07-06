__author__ = 'NamelessOne'

# import consts
import urllib.request
import datetime
import json

start = datetime.datetime.now()
end = start + datetime.timedelta(days=3)
response = urllib.request.urlopen("https://www.googleapis.com/calendar/v3/calendars/fantasyradioru@gmail.com/events?"
                                 "key=AIzaSyDam413Hzm4l8GOEEg-NF8w8wdAbUsKEjM&maxResults=50&singleEvents=true&"
                                 "orderBy=startTime&timeMin=" + start.strftime('%Y-%m-%dT') + '00:00:00.000Z&timeMax='
                                 + end.strftime('%Y-%m-%dT') + '00:00:00.000Z')
s = str(response.read().decode('utf-8'))
json.loads(s)
#for i in range(0, len(s)):
#    print(s[i])
#print(s)