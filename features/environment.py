import os
import logging
import datetime
import shutil
from time import sleep
from appium import webdriver
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from utilities.jira import jira
from behave.model_core import Status

def before_all(context):
    jira.connect_to_jira()
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


def before_scenario(context, scenario):
    logging.info("START scenario: " + scenario.name)

def after_step(context, step):

    if step.status == "failed":
        attach(context.driver.get_screenshot_as_png(), name=datetime.datetime.now().timestamp(), attachment_type = AttachmentType.PNG)
        # jira.attach_screenshots_in_jira(context.driver.capture_screenshots_for_jira())


def after_scenario(context, scenario):
    logging.info(scenario.status)
    if scenario.status == Status.failed:

        scenario_name = "Scenario Name: " + scenario.name
        description = ""
        for step in scenario.steps:
            rows = ""
            description += str(step) + "\n"
            if step.table is not None:
                rows = '\n'.join(str(row) for row in step.table.rows)
                rows = rows.replace("Row [", "")
                rows = rows.replace("]", "")
                description += str(rows) + "\n"
        description = description.replace("<", "")
        description = description.replace(">", "")

        # jira.add_issue(scenario_name, description)

    logging.info("FINISHED scenario: " + scenario.name)





def capture_screenshots_for_jira(context):
    path = os.getcwd()+"/temp"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    path_to_capture_screenshot = path+"/"+str(datetime.datetime.now().timestamp())+".png"
    context.driver.get_screenshot_as_file(path_to_capture_screenshot)
    return path_to_capture_screenshot