from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import when, given,then


# init driver
@given('Open Amazon bestsellers')
def open_help_center(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('The 1 links are Present')
def verify_1link(context):
    expected_result1 = 'Amazon Best Sellers'
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text').text
    assert expected_result1 == actual_result1, f"expected text {expected_result1} is same as {actual_result1}"
#################################################################################################################
# hot new releases
@when('Click on 2link')
def click_2link(context):
    search = context.driver.find_element(By.CSS_SELECTOR,'a[href*="/gp/new-releases/ref=zg_bs_tab"]')
    search.click()

@then('The 2 links are Present')
def verify_2link(context):
    expected_result1 = 'Amazon Hot New Releases'
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text').text
    assert expected_result1 == actual_result1, f"expected text {expected_result1} is same as {actual_result1}"
    sleep(2)
#####################################################################################################################
# movers and shakers
@when('Click on 3link')
def click_3link(context):
    search1 = context.driver.find_element(By.CLASS_NAME, '_p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP')
    search1.click()

@then('The 3 links are Present')
def verify_3link(context):
    expected_result1 = 'Amazon Movers & Shakers'
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR,'#zg_banner_text').text
    assert expected_result1 == actual_result1, f"expected text {expected_result1} is same as {actual_result1}"
##########################################################################################################################
#most gifted
@when('Click on 4link')
def click_4link(context):
    search3 = context.driver.find_element(By.CSS_SELECTOR,'a[href*="/gp/most-wished-for/ref=zg_mw_tab')
    search3.click()

@then('The 4 links are Present')
def verify_4link(context):
    expected_result1 = 'Amazon Most Wished For'
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text').text
    assert expected_result1 == actual_result1, f"expected text {expected_result1} is same as {actual_result1}"
###########################################################################################################
# gift ideas
@when('Click on 5link')
def click_5link(context):
    search4 = context.driver.find_element(By.CSS_SELECTOR,'a[href*="/gp/most-gifted/ref=zg_mw_tab')
    search4.click()

@then('The 5 links are Present')
def verify_5link(context):
    expected_result1 = 'Amazon Gift Ideas'
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text').text
    assert expected_result1 == actual_result1, f"expected text {expected_result1} is same as {actual_result1}"
    sleep(4)
    print('Test Passed')
    context.driver.quit()