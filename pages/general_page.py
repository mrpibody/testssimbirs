from pages.base_page import BasePage
from pages.locators import GeneralPageLocators
from selenium.webdriver.common.by import By

class GeneralPage(BasePage):

    def go_to_calc_page(self):
        textarea = self.browser.find_element(By.NAME, "q")
        textarea.send_keys("Калькулятор\n")

    def calc_exem(self):
        numbarea = self.browser.find_element(By.CLASS_NAME, "jlkklc")
        numbarea.send_keys("1*2-3+1\n")

    def should_be_mem(self):
        assert self.is_element_present(*GeneralPageLocators.mem), "example is none"

    def should_be_resp(self):
        assert self.is_element_present(*GeneralPageLocators.resp), "Number is none"
