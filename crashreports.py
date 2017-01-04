__author__ = 'NamelessOne'

import consts
import pymysql
import CrashReport
import cgi


def add(environ):
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.

    report = CrashReport.CrashReport(form)

    response_body = ""
    # Connect to base
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
        response_body += s
        return response_body
    cur = conn.cursor()
    if len(report.report_id) == 0:
        response_body += "empty report"
        return response_body
    try:
        cur.execute("INSERT INTO CrashReports(REPORT_ID, APP_VERSION_CODE, APP_VERSION_NAME, PACKAGE_NAME, FILE_PATH, "
                    "PHONE_MODEL, BRAND, PRODUCT, ANDROID_VERSION, BUILD, TOTAL_MEM_SIZE, AVAILABLE_MEM_SIZE, "
                    "CUSTOM_DATA, IS_SILENT, STACK_TRACE, INITIAL_CONFIGURATION, CRASH_CONFIGURATION, DISPLAY, "
                    "USER_COMMENT, USER_EMAIL, USER_APP_START_DATE, USER_CRASH_DATE, DUMPSYS_MEMINFO, LOGCAT, "
                    "INSTALLATION_ID, DEVICE_FEATURES, ENVIRONMENT, SHARED_PREFERENCES, SETTINGS_SYSTEM, "
                    "SETTINGS_SECURE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                    "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (report.report_id.encode('utf-8'), report.app_version_code.encode('utf-8'),
                     report.app_version_name.encode('utf-8'), report.package_name.encode('utf-8'),
                     report.file_path.encode('utf-8'), report.phone_model.encode('utf-8'),
                     report.brand.encode('utf-8'),
                     report.product.encode('utf-8'), report.android_version.encode('utf-8'),
                     report.build.encode('utf-8'), report.total_mem_size.encode('utf-8'),
                     report.available_mem_size.encode('utf-8'), report.custom_data.encode('utf-8'),
                     report.is_silent.encode('utf-8'), report.stack_trace.encode('utf-8'),
                     report.initial_configuration.encode('utf-8'),
                     report.crash_configuration.encode('utf-8'), report.display.encode('utf-8'),
                     report.user_comment.encode('utf-8'),
                     report.user_email.encode('utf-8'), report.user_app_start_date.encode('utf-8'),
                     report.user_crash_date.encode('utf-8'), report.dumpsys_meminfo.encode('utf-8'),
                     report.logcat.encode('utf-8'), report.installation_id.encode('utf-8'),
                     report.device_features.encode('utf-8'), report.environment.encode('utf-8'),
                     report.shared_preferences.encode('utf-8'),
                     report.settings_system.encode('utf-8'), report.settings_secure.encode('utf-8')))
    except pymysql.DataError as e:
        # Ошибки MySQL всегда четырехразрядные, помни об этом!!!
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


def build_reports_table(params=None):
    if params is None:
        params = {}
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
    except Exception as e:
        s = str(e)
        return s
    cur = conn.cursor()
    try:
        where = ''
        if len(params) != 0:
            where = ' WHERE '
            for i, key, value in params.items():
                where += key + ' LIKE \'%' + value[0] + '%\''
                if i != len(params) - 1:
                    where += ' AND '
        cur.execute('SELECT * FROM CrashReports' + where)
        field_names = [i[0] for i in cur.description]
        field_names.append("action")
        rows = cur.fetchall()
        rows = [(elem + ("<a href=\"/delete?id=" + elem[0] + "\">Delete</a>",)) for elem in rows]
        result = __build_html_table(field_names, rows)
        return result
    except Exception as e:
        return e


def delete_report_by_id(report_id):
    try:
        conn = pymysql.connect(host=consts.HOST, port=3306, user=consts.USER, passwd=consts.PASSWORD, db=consts.DB)
        cur = conn.cursor()
        cur.execute('DELETE FROM CrashReports WHERE REPORT_ID = %s', (report_id,))
        conn.commit()
    finally:
        conn.close()
        cur.close()


def __build_html_table(column_names, rows):
    result = "<tr>"
    for name in column_names:
        result += "<td>" + name + "</td>"
    result += "</tr>"
    for row in rows:
        result += "<tr>"
        for elem in row:
            result += "<td>" + str(elem) + "</td>"
        result += "</tr>"
    return result
