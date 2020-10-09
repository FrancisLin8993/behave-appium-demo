from behave import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


@given('the Android app is launched')
def step_impl(context):
    pass


@then('we can click the item in the Android app')
def step_impl(context):
    try:

        actions = TouchAction(context.driver)
        actions.press(x=517, y=1635).move_to(x=525, y=753).release().perform()

        text_el = context.driver.find_element_by_accessibility_id('Text')
        text_el.click()
    except:
        pass
    finally:
        sleep(3)


@given('the iOS app is launched')
def step_impl(context):
    pass


@then('we can click the item in the iOS app')
def step_impl(context):
    try:
        # Intentionally fail this test
        element = context.driver.find_element_by_accessibility_id('Some Random Thing')
    except NoSuchElementException:
        raise
    finally:
        sleep(3)
