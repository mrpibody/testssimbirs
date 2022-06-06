from pages.base_page import BasePage
from pages.locators import GeneralPageLocators


class GeneralPage(BasePage):

    def go_to_calc_page(self):
        textarea = self.browser.find_element(*GeneralPageLocators.textarea)
        textarea.send_keys("Калькулятор")

    def send_resp(self):
        button = self.browser.find_element(*GeneralPageLocators.button)
        button.click()

    def calc_exam(self):
        numbarea = self.browser.find_element(*GeneralPageLocators.numbarea)
        numbarea.send_keys("1*2-3+1\n")

    def should_be_mem(self):
        assert self.browser.find_element(*GeneralPageLocators.mem).text == "1 × 2 - 3 + 1 =", 'Unexpected value'

    def should_be_resp(self):
        assert self.browser.find_element(*GeneralPageLocators.resp).text == "0", 'Unexpected value'

