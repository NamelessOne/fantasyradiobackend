__author__ = 'NamelessOne'
from cgi import parse_qs, escape


class CrashReport:
    def __init__(self, parameters):
        if 'REPORT_ID' in parameters:
            self.report_id = parameters.get('REPORT_ID')[0]
        if 'APP_VERSION_CODE' in parameters:
            self.app_version_code = parameters.get('APP_VERSION_CODE', [''])[0]
        if 'APP_VERSION_NAME' in parameters:
            self.app_version_name = parameters.get('APP_VERSION_NAME', [''])[0]
        if 'PACKAGE_NAME' in parameters:
            self.package_name = parameters.get('PACKAGE_NAME', [''])[0]
        if 'FILE_PATH' in parameters:
            self.file_path = parameters.get('REPORT_ID', [''])[0]
        if 'PHONE_MODEL' in parameters:
            self.phone_model = parameters.get('REPORT_ID', [''])[0]
        if 'BRAND' in parameters:
            self.brand = parameters.get('REPORT_ID', [''])[0]
        if 'PRODUCT' in parameters:
            self.product = parameters.get('REPORT_ID', [''])[0]
        if 'ANDROID_VERSION' in parameters:
            self.android_version = parameters.get('REPORT_ID', [''])[0]
        if 'BUILD' in parameters:
            self.build = parameters.get('REPORT_ID', [''])[0]
        if 'TOTAL_MEM_SIZE' in parameters:
            self.total_mem_size = parameters.get('REPORT_ID', [''])[0]
        if 'AVAILABLE_MEM_SIZE' in parameters:
            self.available_mem_size = parameters.get('REPORT_ID', [''])[0]
        if 'CUSTOM_DATA' in parameters:
            self.custom_data = parameters.get('REPORT_ID', [''])[0]
        if 'IS_SILENT' in parameters:
            self.is_silent = parameters.get('REPORT_ID', [''])[0]
        if 'STACK_TRACE' in parameters:
            self.stack_trace = parameters.get('REPORT_ID', [''])[0]
        if 'INITIAL_CONFIGURATION' in parameters:
            self.initial_configuration = parameters.get('REPORT_ID', [''])[0]
        if 'CRASH_CONFIGURATION' in parameters:
            self.crash_configuration = parameters.get('REPORT_ID', [''])[0]
        if 'DISPLAY' in parameters:
            self.display = parameters.get('REPORT_ID', [''])[0]
        if 'USER_COMMENT' in parameters:
            self.user_comment = parameters.get('REPORT_ID', [''])[0]
        if 'USER_EMAIL' in parameters:
            self.user_email = parameters.get('REPORT_ID', [''])[0]
        if 'USER_APP_START_DATE' in parameters:
            self.user_app_start_date = parameters.get('REPORT_ID', [''])[0]
        if 'USER_CRASH_DATE' in parameters:
            self.user_crash_date = parameters.get('REPORT_ID', [''])[0]
        if 'DUMPSYS_MEMINFO' in parameters:
            self.dumpsys_meminfo = parameters.get('REPORT_ID', [''])[0]
        if 'LOGCAT' in parameters:
            self.logcat = parameters.get('REPORT_ID', [''])[0]
        if 'INSTALLATION_ID' in parameters:
            self.installation_id = parameters.get('REPORT_ID', [''])[0]
        if 'DEVICE_FEATURES' in parameters:
            self.device_features = parameters.get('REPORT_ID', [''])[0]
        if 'ENVIRONMENT' in parameters:
            self.environment = parameters.get('REPORT_ID', [''])[0]
        if 'SHARED_PREFERENCES' in parameters:
            self.shared_preferences = parameters.get('REPORT_ID', [''])[0]
        if 'SETTINGS_SYSTEM' in parameters:
            self.settings_system = parameters.get('REPORT_ID', [''])[0]
        if 'SETTINGS_SECURE' in parameters:
            self.settings_secure = parameters.get('REPORT_ID', [''])[0]