link = "http://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/"

def test_is_button_exist(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".add-to-basket .btn")

