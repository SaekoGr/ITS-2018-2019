#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def before_all(context):  
    dp = {'browserName': 'firefox', 'marionette': 'true', 'javascriptEnabled': 'true'}
    context.browser = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub', desired_capabilities=dp)
    context.browser.implicitly_wait(5)
    context.base_url = "http://mys01.fit.vutbr.cz:8012"
    context.is_logged_in = False
    context.is_in_cart = False


def after_all(context):  
    context.browser.quit() 