import pytest
from pages.general_page import GeneralPage

@pytest.mark.smoke
def test_open_calc(browser):
    url = "http://google.com"
    page = GeneralPage(browser, url)
    page.open()
    page.go_to_calc_page()
    page.calc_exem()
    page.should_be_mem()
    page.should_be_resp()
