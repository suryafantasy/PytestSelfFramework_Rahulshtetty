from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyElementLocated(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
    def selectOptionByTest(self,text):
        select = Select(self.driver.find_element(By.XPATH, "//*[@id='exampleFormControlSelect1']"))
        select.select_by_visible_text(text)