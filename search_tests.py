from behave import *

@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.get('http://www.lazada.vn')
@when('I search for {text}')
def step_i_search_for(context,text):
    search_field = context.driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys(text)
    search_field.submit()
@then('I should see a list of matching products in search result')
def step_i_should_see_list(context):
    products = context.driver.find_element_by_xpath("//div[@class='c2prKC']")
    assert len(products) >0