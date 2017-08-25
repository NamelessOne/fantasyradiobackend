_author__ = 'NamelessOne'
import os

HOST = os.environ['OPENSHIFT_MYSQL_DB_HOST']
USER = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
PASSWORD = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
DB = os.environ['OPENSHIFT_APP_NAME']
API_KEY = os.environ['OPENSHIFT_APP_NAME']
ADMIN_USER = os.environ['ADMIN_USER']
ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
CALENDAR_URL = "https://www.googleapis.com/calendar/v3/calendars/fantasyradioru@gmail.com/events?" \
               "key=AIzaSyDam413Hzm4l8GOEEg-NF8w8wdAbUsKEjM&maxResults=50&singleEvents=true&orderBy=startTime"
STREAM_INFO_PLAYER_URL = "http://fantasyradio.ru/player.php"
STREAM_INFO_ABOUT_URL = "http://fantasyradio.ru/player_podrobnee.html"
