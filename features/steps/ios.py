from behave import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

@given('the iOS app is launched')
def step_impl(context):
    pass


@then('we can click the item in the iOS app')
def step_impl(context):
    try:
        el = context.driver.find_element_by_xpath('//*[@elementId="23000000-0000-0000-1845-000000000000"]')
        el.click()
    except:
        pass
    finally:
        sleep(3)
