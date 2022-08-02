import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass): #passing parent class here so that no need to use fixture since parent class contains setup fixture
    def test_e2e(self):
        homepage=HomePage(self.driver) #creating object
        self.driver.implicitly_wait(5)
        homepage.searchItems().send_keys("be")
        time.sleep(2)
        actual_list = []
        products_list=homepage.product_list()
        #products_list = self.driver.find_elements(By.XPATH, "//div/h4[@class='product-name']")
        for product in products_list:
            actual_list.append(product.text)
        #print(actual_list)

        list_carts = self.driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
        leng = len(list_carts)
        for carts in list_carts:
            if leng > 0:
                carts.click()
                leng = leng - 1
        self.driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
        self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        self.driver.set_page_load_timeout(2)
        self.driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
        self.verifyElementLocated("promoCode")
        #wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()
        self.verifyElementLocated("promoInfo")
        #wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))
        promocode = self.driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
        print(promocode)


