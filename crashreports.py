__author__ = 'NamelessOne'

import os
import pymysql
import CrashReport
from cgi import parse_qs, escape

host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
password = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
db = os.environ['OPENSHIFT_APP_NAME']

def add(self, environ):
    # Get data from fields
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    report = CrashReport(parameters)
    response_body = ""
    #TODO собственно тут парсим кучу параметров

    #Connect to base
    try:
        conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=db)
    except Exception as e:
        s = str(e)
        response_body += s
        return response_body
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO CrashReports(REPORT_ID, APP_VERSION_CODE, APP_VERSION_NAME, PACKAGE_NAME, FILE_PATH, "
                    "PHONE_MODEL, BRAND, PRODUCT, ANDROID_VERSION, BUILD, TOTAL_MEM_SIZE, AVAILABLE_MEM_SIZE, "
                    "CUSTOM_DATA, IS_SILENT, STACK_TRACE, INITIAL_CONFIGURATION, CRASH_CONFIGURATION, DISPLAY, "
                    "USER_COMMENT, USER_EMAIL, USER_APP_START_DATE, USER_CRASH_DATE, DUMPSYS_MEMINFO, LOGCAT, "
                    "INSTALLATION_ID, DEVICE_FEATURES, ENVIRONMENT, SHARED_PREFERENCES, SETTINGS_SYSTEM, "
                    "SETTINGS_SECURE) VALUES (%s,%s)", (report.report_id, report.app_version_code,
                    report.app_version_name, report.package_name, report.file_path, report.phone_model, report.brand,
                    report.product, report.android_version, report.build, report.total_mem_size,
                    report.available_mem_size, report.custom_data, report.is_silent, report.stack_trace,
                    report.initial_configuration, report.crash_configuration, report.display, report.user_comment,
                    report.user_email, report.user_app_start_date, report.user_crash_date, report.dumpsys_meminfo,
                    report.logcat, report.installation_id, report.device_features, report.environment,
                    report.shared_preferences, report.settings_system, report.settings_secure))
    except pymysql.DataError as e:
        #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.IntegrityError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.ProgrammingError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    except pymysql.NotSupportedError as e:
        s = str(e.args[0])
        response_body += "-" + s[1] + s[2] + s[3] + s[4]
        return response_body
    conn.commit()
    cur.close()
    conn.close()
    return response_body