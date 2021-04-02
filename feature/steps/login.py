from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'in twitter login page')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.button_signup)
    context.browser.find_element(By.XPATH,locator.button_login_1).click()
    sleep(2)

@when(u'enter valid username and password')
def step_impl(context):
    username = context.config.userdata.get("username")
    password = context.config.userdata.get("password")
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.NAME,locator.input_username).send_keys(username)
    sleep(2)
    context.browser.find_element(By.NAME,locator.input_password).send_keys(password)

@when(u'click login button')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login_2).click()

@then(u'success login')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_tweet)
