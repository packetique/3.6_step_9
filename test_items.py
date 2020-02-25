

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket_is_enabled(browser):
    browser.get(link)
    btn = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert btn.is_enabled, "Button not found!!!"
