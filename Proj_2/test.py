#!/usr/bin/env python3

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriverFirefox(unittest.TestCase):
    def setUp(self):
        dp = {'browserName': 'firefox', 'marionette': 'true',
                'javascriptEnabled': 'true'}
        self.driver = webdriver.Remote(
                command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
                desired_capabilities=dp)
        self.driver.implicitly_wait(15)
        self.base_url = "http://mys01.fit.vutbr.cz:8012/"
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def tearDown(self):
        self.driver.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/logout")
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()