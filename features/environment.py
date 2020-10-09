import os
from time import sleep

from appium import webdriver


def before_all(context):
    context.config.setup_logging()
    pass

def before_feature(context, feature):

    if 'iOS' in feature.tags:
        app = os.path.join(os.path.dirname(__file__), '../apps/ios/UIKitCatalog', 'UIKitCatalog-iphonesimulator.zip')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4724/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'deviceName': 'iPhone 11',
                'platformVersion': '13.7',
                'automationName': 'XCUITest',
                'noReset': 'true'
            })

    elif 'android' in feature.tags:
        app = os.path.join(os.path.dirname(__file__),
                           '../apps/Android/',
                           'ApiDemos-debug.apk')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '11.0',
                'deviceName': 'emulator-5554',
                'appActivity': '.ApiDemos',
                'appPackage': 'io.appium.android.apis',
                'automationName': 'UiAutomator2',
                'uiautomator2ServerInstallTimeout': '60000'
            })



def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()