import pytest
from pages.general_page import GeneralPage

@pytest.mark.smoke
def test_open_calc(browser):
    url = "http://google.com"
    page = GeneralPage(browser, url)
    page.open()
    page.go_to_calc_page()
    page.send_resp()
    page.calc_exam()
    page.should_be_mem()
    assert should_be_mem() == "1 × 2 - 3 + 1 =", 'Unexpected value'
    page.should_be_resp()
    assert should_be_resp() == "0", 'Unexpected value'
