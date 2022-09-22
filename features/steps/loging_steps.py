from multiprocessing import context
from behave import given, then, when
from features.page_objects.BasePage import (click_element_by_css_selector,
                                            send_keys_by_css_selector, element_displayed, 
                                            wait_until_url_changes)
from features.page_objects.login_page import (EXPECTEDHOME_URL, LOGIN_BTN, LOGIN_URL,
                                              PASSWORD_FIELD, USERNAME_FIELD)
from features.utils.CommonConstants import VALID_PASSWORD, VALID_USERNAME
from utils.Driver import launch_browser
from features.page_objects.BasePage import 
from features.utils.CommonConstants import LOGOUT_BUTTON
from features.page_objects.BasePage import element_displayed


@given('the user is on demoblaze.com')
def navigate_to_demoblaze(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get('https://demoblaze.com/index.html')

@when('the user logs in')
def login_with_valid_credentials(context) :
    click_element_by_css_selector(context, LOGIN_BTN)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, VALID_PASSWORD)
    
@then('the page displays the button log out')
def logout_button = element_displayed(context, LOGOUT_BUTTON) :
    assert LOGOUT_BUTTON == True