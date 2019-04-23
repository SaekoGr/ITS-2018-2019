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

def after_tag(context, tag):
    if tag.startswith("clear_wish_list"):
        context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")
        context.browser.find_element_by_xpath("//td[6]/a/i").click()
    if tag.startswith("clear_cart"):
        context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
        context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()
    if tag.startswith("log_out"):
        context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a").click()
        context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/ul/li[5]/a").click()


def after_all(context):  
    context.browser.quit() 
