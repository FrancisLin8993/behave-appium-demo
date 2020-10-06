from behave import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

@given('the app is launched')
def step_impl(context):
    pass


@then('we can click the item')
def step_impl(context):
    try:

        actions = TouchAction(context.driver)
        actions.press(x=517, y=1635).move_to(x=525, y=753).release().perform()

        textEl = context.driver.find_element_by_accessibility_id('Text')
        textEl.click()
    except:
        pass
    finally:
        sleep(3)
