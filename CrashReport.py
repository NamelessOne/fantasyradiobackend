__author__ = 'NamelessOne'
from cgi import parse_qs, escape

class CrashReport:
    def __init__(self, parameters):
        if 'REPORT_ID' in parameters:
            self.report_id = escape(parameters['REPORT_ID'][0])
        if 'APP_VERSION_CODE' in parameters:
            self.app_version_code = escape(parameters['APP_VERSION_CODE'][0])
        if 'APP_VERSION_NAME' in parameters:
            self.app_version_name = escape(parameters['APP_VERSION_NAME'][0])
        if 'PACKAGE_NAME' in parameters:
            self.package_name = escape(parameters['PACKAGE_NAME'][0])
        if 'FILE_PATH' in parameters:
            self.file_path = escape(parameters['FILE_PATH'][0])
        if 'PHONE_MODEL' in parameters:
            self.phone_model = escape(parameters['PHONE_MODEL'][0])
        if 'BRAND' in parameters:
            self.brand = escape(parameters['BRAND'][0])
        if 'PRODUCT' in parameters:
            self.product = escape(parameters['PRODUCT'][0])
        if 'ANDROID_VERSION' in parameters:
            self.android_version = escape(parameters['ANDROID_VERSION'][0])
        if 'BUILD' in parameters:
            self.build = escape(parameters['BUILD'][0])
        if 'TOTAL_MEM_SIZE' in parameters:
            self.totla_mem_size = escape(parameters['TOTAL_MEM_SIZE'][0])
        if 'AVAILABLE_MEM_SIZE' in parameters:
            self.available_mem_size = escape(parameters['AVAILABLE_MEM_SIZE'][0])
        if 'CUSTOM_DATA' in parameters:
            self.custom_data = escape(parameters['CUSTOM_DATA'][0])
        if 'IS_SILENT' in parameters:
            self.is_silent = escape(parameters['IS_SILENT'][0])
        if 'STACK_TRACE' in parameters:
            self.stack_trace = escape(parameters['STACK_TRACE'][0])
        if 'INITIAL_CONFIGURATION' in parameters:
            self.initial_configuration = escape(parameters['INITIAL_CONFIGURATION'][0])
        if 'CRASH_CONFIGURATION' in parameters:
            self.crash_configuration = escape(parameters['CRASH_CONFIGURATION'][0])
        if 'DISPLAY' in parameters:
            self.display = escape(parameters['DISPLAY'][0])
        if 'USER_COMMENT' in parameters:
            self.user_comment = escape(parameters['USER_COMMENT'][0])
        if 'USER_EMAIL' in parameters:
            self.user_email = escape(parameters['USER_EMAIL'][0])
        if 'USER_APP_START_DATE' in parameters:
            self.user_app_start_date = escape(parameters['USER_APP_START_DATE'][0])
        if 'USER_CRASH_DATE' in parameters:
            self.user_crash_date = escape(parameters['USER_CRASH_DATE'][0])
        if 'DUMPSYS_MEMINFO' in parameters:
            self.dumpsys_meminfo = escape(parameters['DUMPSYS_MEMINFO'][0])
        if 'LOGCAT' in parameters:
            self.logcat = escape(parameters['LOGCAT'][0])
        if 'INSTALLATION_ID' in parameters:
            self.installation_id = escape(parameters['INSTALLATION_ID'][0])
        if 'DEVICE_FEATURES' in parameters:
            self.device_features = escape(parameters['DEVICE_FEATURES'][0])
        if 'ENVIRONMENT' in parameters:
            self.environment = escape(parameters['ENVIRONMENT'][0])
        if 'SHARED_PREFERENCES' in parameters:
            self.shared_preferences = escape(parameters['SHARED_PREFERENCES'][0])
        if 'SETTINGS_SYSTEM' in parameters:
            self.settings_system = escape(parameters['SETTINGS_SYSTEM'][0])
        if 'SETTINGS_SECURE' in parameters:
            self.settings_secure = escape(parameters['SETTINGS_SECURE'][0])