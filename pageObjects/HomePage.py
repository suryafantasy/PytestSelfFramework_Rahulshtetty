from selenium.webdriver.common.by import By
class HomePage:
    search=(By.CSS_SELECTOR,"input[class='search-keyword']")
    product=(By.XPATH,"//div/h4[@class='product-name']")
    name=(By.NAME, 'name')
    email=(By.NAME, 'email')
    def __init__(self,driver):
        self.driver=driver

    def searchItems(self):
        return self.driver.find_element(*HomePage.search)
    def product_list(self):
        return self.driver.find_elements(*HomePage.product)
    def getname(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)



    # self.driver.implicitly_wait(5)
    # self.driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("be")
    # time.sleep(2)
    #
    # actual_list = []
    # products_list = self.driver.find_elements(By.XPATH, "//div/h4[@class='product-name']")