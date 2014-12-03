__author__ = 'NamelessOne'
from cgi import parse_qs, escape

class CrashReport:
    def __init__(self, parameters):
        if 'REPORT_ID' in parameters:
            self.report_id = escape(parameters['reportId'][0])
        if 'APP_VERSION_CODE' in parameters:
            self.app_version_code = escape(parameters['appVersionCode'][0])
        if 'APP_VERSION_NAME' in parameters:
            self.app_version_name = escape(parameters['appVersionName'][0])
        if 'PACKAGE_NAME' in parameters:
            self.package_name = escape(parameters['packageName'][0])
        if 'FILE_PATH' in parameters:
            self.file_path = escape(parameters['filePath'][0])
        if 'PHONE_MODEL' in parameters:
            self.phone_model = escape(parameters['phoneModel'][0])
        if 'BRAND' in parameters:
            self.brand = escape(parameters['brand'][0])
        if 'PRODUCT' in parameters:
            self.product = escape(parameters['product'][0])
        if 'ANDROID_VERSION' in parameters:
            self.android_version = escape(parameters['androidVersion'][0])
        if 'BUILD' in parameters:
            self.build = escape(parameters['build'][0])
        if 'TOTAL_MEM_SIZE' in parameters:
            self.totla_mem_size = escape(parameters['totalMemSize'][0])
        if 'AVAILABLE_MEM_SIZE' in parameters:
            self.available_mem_size = escape(parameters['availableMemSize'][0])
        if 'CUSTOM_DATA' in parameters:
            self.custom_data = escape(parameters['customData'][0])
        if 'IS_SILENT' in parameters:
            self.is_silent = escape(parameters['isSilent'][0])
        if 'STACK_TRACE' in parameters:
            self.stack_trace = escape(parameters['stackTrace'][0])
        if 'INITIAL_CONFIGURATION' in parameters:
            self.initial_configuration = escape(parameters['initialConfiguration'][0])
        if 'CRASH_CONFIGURATION' in parameters:
            self.crash_configuration = escape(parameters['crashConfiguration'][0])
        if 'DISPLAY' in parameters:
            self.display = escape(parameters['display'][0])
        if 'USER_COMMENT' in parameters:
            self.user_comment = escape(parameters['userComment'][0])
        if 'USER_EMAIL' in parameters:
            self.user_email = escape(parameters['userEmail'][0])
        if 'USER_APP_START_DATE' in parameters:
            self.user_app_start_date = escape(parameters['userAppStartDate'][0])
        if 'USER_CRASH_DATE' in parameters:
            self.user_crash_date = escape(parameters['userCrashDate'][0])
        if 'DUMPSYS_MEMINFO' in parameters:
            self.dumpsys_meminfo = escape(parameters['dumpSysMemInfo'][0])
        if 'LOGCAT' in parameters:
            self.logcat = escape(parameters['logcat'][0])
        if 'INSTALLATION_ID' in parameters:
            self.installation_id = escape(parameters['installationId'][0])
        if 'DEVICE_FEATURES' in parameters:
            self.device_features = escape(parameters['deviceFeatures'][0])
        if 'ENVIRONMENT' in parameters:
            self.environment = escape(parameters['environment'][0])
        if 'SHARED_PREFERENCES' in parameters:
            self.shared_preferences = escape(parameters['sharedPreferences'][0])
        if 'SETTINGS_SYSTEM' in parameters:
            self.settings_system = escape(parameters['settingsSystem'][0])
        if 'SETTINGS_SECURE' in parameters:
            self.settings_secure = escape(parameters['settingsSecure'][0])