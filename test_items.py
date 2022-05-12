import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_button_exist_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    btn = browser.find_element_by_css_selector(".add-to-basket .btn")
    expected = ["Añadir al carrito", "Ajouter au panier", "In Warenkorb legen",]
    assert btn.get_attribute("value") in expected, f"Button Add-to-basket has a different name as {expected}"

