__author__ = 'NamelessOne'

class CrashReport:
    def __init__(self, parameters):
        self.report_id = parameters.get('REPORT_ID', '')
        self.app_version_code = parameters.get('APP_VERSION_CODE', '')
        self.app_version_name = parameters.get('APP_VERSION_NAME', '')
        self.package_name = parameters.get('PACKAGE_NAME', '')
        self.file_path = parameters.get('FILE_PATH', '')
        self.phone_model = parameters.get('PHONE_MODEL', '')
        self.brand = parameters.get('BRAND', '')
        self.product = parameters.get('PRODUCT', '')
        self.android_version = parameters.get('ANDROID_VERSION', '')
        self.build = parameters.get('BUILD', '')
        self.total_mem_size = parameters.get('TOTAL_MEM_SIZE', '')
        self.available_mem_size = parameters.get('AVAILABLE_MEM_SIZE', '')
        self.custom_data = parameters.get('CUSTOM_DATA', '')
        self.is_silent = parameters.get('IS_SILENT', '')
        self.stack_trace = parameters.get('STACK_TRACE', '')
        self.initial_configuration = parameters.get('INITIAL_CONFIGURATION', '')
        self.crash_configuration = parameters.get('CRASH_CONFIGURATION', '')
        self.display = parameters.get('DISPLAY', '')
        self.user_comment = parameters.get('USER_COMMENT', '')
        self.user_email = parameters.get('USER_EMAIL', '')
        self.user_app_start_date = parameters.get('USER_APP_START_DATE', '')
        self.user_crash_date = parameters.get('USER_CRASH_DATE', '')
        self.dumpsys_meminfo = parameters.get('DUMPSYS_MEMINO', '')
        self.logcat = parameters.get('LOGCAT', '')
        self.installation_id = parameters.get('INSTALLATION_ID', '')
        self.device_features = parameters.get('DEVICE_EATURES', '')
        self.environment = parameters.get('ENVIRONMENT', '')
        self.shared_preferences = parameters.get('SHARED_PREFERENCES', '')
        self.settings_system = parameters.get('SETTINGS_SYSTEM', '')
        self.settings_secure = parameters.get('SETTINGS_SECURE', '')