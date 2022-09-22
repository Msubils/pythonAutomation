from behave import given, then, when
from features.utils.Driver import launch_browser
from page_objects.BasePage import get_element_text, click_element_by_css_selector, send_keys_by_css_selector
import time

@given('the user is on demoblaze page')
def navigate_to_demoblaze(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get('https://demoblaze.com/')
  

@when('the user removes an item from the cart')
def remove_item(context) :
    click_element_by_css_selector(context, '#remove-sauce-labs-backpack')

@then('se muestra el mensaje de compra exitosa')
def SUCCESSFUL_PURCHASE_MESSAGE(context) :
    title_text = get_element_text(context, '')
    print(title_text)
    assert title_text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
