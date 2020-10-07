import os
from time import sleep

from appium import webdriver


def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):

    if 'iOS' in feature.tags:
        app = os.path.join(os.path.dirname(__file__), '../apps/ios/UIKitCatalog', 'UIKitCatalog-iphonesimulator.zip')
        app = os.path.abspath(app)
        context.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'deviceName': 'iPhone 11',
                'platformVersion': '13.7',
                'automationName': 'XCUITest',
                'noReset': 'true'
            })



def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()