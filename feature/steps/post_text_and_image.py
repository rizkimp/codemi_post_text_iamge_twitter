import os
from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from hamcrest import *

@given(u'in twitter home page')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_tweet)

@when(u'enter text and upload image')
def step_impl(context):
    text = context.config.userdata.get("text_tweet")
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_tweet).send_keys(text)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.input_file).send_keys(os.getcwd()+ "/assets/bd.jpeg")
    sleep(3)

@when(u'click button tweet')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.button_tweet).click()

@then(u'success post text and image')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.alert_your_tweet_sent)   
