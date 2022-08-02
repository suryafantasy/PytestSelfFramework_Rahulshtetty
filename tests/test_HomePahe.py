import time

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        print(self.driver.current_url)
        self.driver.minimize_window()
        # locators
        # self.driver.find_element(By.NAME, 'name').send_keys('Rahul')
        # self.driver.find_element(By.NAME, 'email').send_keys('helo@gmail.com')
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        self.driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123455')
        self.driver.find_element(By.XPATH, "//*[@id='exampleCheck1']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']").click()
        a = self.driver.find_element(By.XPATH, "//*[@id='exampleFormControlSelect1']")
        # select = Select(self.driver.find_element(By.XPATH, "//*[@id='exampleFormControlSelect1']"))
        # select.select_by_visible_text('Female')
        self.selectOptionByTest('Female')
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        txt = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(txt)
        ###########dynamic dropdown handling
        self.driver.get("https://rahulshettyacademy.com/dropdownsPractise")
        self.driver.find_element(By.ID, "autosuggest").send_keys("Ind")
        time.sleep(2)
        countries = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
        for i in countries:
            if i.text == "India":
                i.click()
                break
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.find_element(By.ID, "name").send_keys("surya")
        self.driver.find_element(By.ID, "alertbtn").click()
        Alert = self.driver.switch_to.alert
        msg = Alert.text
        print(msg)
        assert "surya" in msg
        Alert.accept()
    @pytest.fixture(params=[("Rahul","shetty","male"),("anshika","shetty","female")])
    def getData(self,request):
        return request.param
        # driver.close()
