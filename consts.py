_author__ = 'NamelessOne'
import os

HOST = os.environ['OPENSHIFT_MYSQL_DB_HOST']
USER = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
PASSWORD = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
DB = os.environ['OPENSHIFT_APP_NAME']
API_KEY = "AIzaSyBhk7_8wFJmnIqWUQSDgP5Z-U24Tz5naWk"
ADMIN_USER = 'NamelessOne'
ADMIN_PASSWORD = 'luxextenebris'
CALENDAR_URL = "https://www.googleapis.com/calendar/v3/calendars/fantasyradioru@gmail.com/events?" \
               "key=AIzaSyDam413Hzm4l8GOEEg-NF8w8wdAbUsKEjM&maxResults=50&singleEvents=true&orderBy=startTime"
STREAM_INFO_PLAYER_URL = "http://fantasyradio.ru/player.php"
STREAM_INFO_ABOUT_URL = "http://fantasyradio.ru/player_podrobnee.html"
