import time
import unittest
from datetime import datetime, timedelta
from decimal import Decimal
from unicodedata import decimal

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Caterer(unittest.TestCase):
    def setUp(self):
        # using Chrome browser. ensure it is installed
        #self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1200x600')
        chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
        self.driver = webdriver.Chrome( chrome_options=chrome_options)
        #self.driver.maximize_window()

    def test_bday(self):
        driver = self.driver
        # open cookifi site
        driver.implicitly_wait(10)
        driver.get('https://cookifi.com/')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Caterer")))
        # click on caterer
        caterer = driver.find_element_by_partial_link_text('Caterer').click()
        # fill form
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        date = driver.find_element_by_id("id_when")
        date.click()
        date.clear()
        date.send_keys(tomorrow.strftime("%Y-%m-%d"))
        date.send_keys(Keys.RETURN)
        #time.sleep(2)
        name = driver.find_element_by_id('id_name')
        name.click()
        name.send_keys('Testing Name')
        location = driver.find_element_by_id('id_location')
        location.click()
        location.send_keys('testing location')
        email = driver.find_element_by_id('id_email')
        email.click()
        email.send_keys('cookifi.test@gmail.com')
        mobile = driver.find_element_by_id('id_mobile')
        mobile.click()
        mobile.send_keys('9833568580')

        submit = driver.find_element_by_id('id_submit')
        #actions = ActionChains(driver)
        #actions.move_to_element(submit).perform()

        driver.execute_script("arguments[0].scrollIntoView();", submit)
        #driver.execute_script("window.scrollBy(0, -20);")
        #time.sleep(4)
        submit.click()


if __name__ == '__main__':
    unittest.main()

